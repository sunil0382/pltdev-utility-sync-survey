import grpc
from sqlalchemy import text
from app.config.settings import SCHEMA
from app.database.session import get_db
from app.models import UtilityServiceRequest
from app.schemas.nbiot_schema import NBIOTCoverage
from app.schemas.premise_schema import PremiseInfo
from app.schemas.ptw_schema import PTWInfo
from app.schemas.survey_details_schema import SurveyDetails
from app.schemas.survey_gateway_schema import SurveyGatewaySchema
from app.stubs.survey_requirements import survey_requirements_pb2
from app.stubs.utility_request import utility_request_pb2, utility_request_pb2_grpc
from app.services.managers.survey_manager import SurveyManager


class UtilityServices(utility_request_pb2_grpc.UtilityServicesServicer):
    """
    gRPC service implementation for managing and listing utility services.
    """

    def FetchUtilityRequest(self, request, context):
        """
        Fetches a utility service request based on the provided utility number.

        Args:
            request: gRPC request containing the utility number.
            context: gRPC context for error handling and metadata.

        Returns:
            UtilityServiceResponse: A response object containing
            details of the utility service request.
        """
        with get_db() as db_session:
            # Query the utility service request by utility number
            utility_request = (
                db_session.query(UtilityServiceRequest)
                .filter(UtilityServiceRequest.utility_number == request.utility_number)
                .first()
            )

            # If the utility request is not found, set an appropriate error response
            if utility_request is None:
                context.set_details(
                    f"Utility request with slug '{request.utility_number}' not found."
                )
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return utility_request_pb2.UtilityServiceResponse()

            survey_manager = SurveyManager(db_session)
            survey_details = survey_manager.get_survey_details(request.utility_number)
            print(survey_details)
            # Execute a SQL function to get survey details based on the utility number
            utility_request_query = text(
                f"SELECT * from "
                f"{SCHEMA}.fn_get_survey_by_utility_number(:utility_number)"
            )
            utility_result = db_session.execute(
                utility_request_query, {"utility_number": str(request.utility_number)}
            )
            results = utility_result.fetchone()
            if results:
                # Unpack the results into respective variables
                utility_number, account_number, region, survey_details, status = results

                # Extracting details from the survey_details dictionary
                premise_info = survey_details.get("premise_info", {})
                nb_oit = survey_details.get("nb_iot_coverage", {})
                requirements = survey_details.get("requirements", {})
                ptw = survey_details.get("ptw", {})
                survey_gateways = survey_details.get("gateways")

                # Constructing the UtilityServiceResponse
                utility_service_response = utility_request_pb2.UtilityServiceResponse(
                    account_number=account_number,
                    utility_number=utility_number,
                    status=status,
                    survey_details=SurveyDetails.from_dict(survey_details),
                    premise_info=PremiseInfo.from_dict(premise_info),
                    nb_oit=NBIOTCoverage.from_dict(nb_oit),
                    ptw_info=PTWInfo.from_dict(ptw),
                )

                # Adding survey gateway details to the response
                for survey_gateway in survey_gateways:
                    _survey_gateway = SurveyGatewaySchema.from_dict(survey_gateway)
                    utility_service_response.survey_gateways.append(_survey_gateway)

                # Adding survey requirements to the response
                for requirement in requirements:
                    survey_requirement = survey_requirements_pb2.SurveyRequirements(
                        slug=str(requirement.get("survey_requirement_slug", "")),
                        requirement_key=requirement.get("requirement_key", None),
                        is_electric=requirement.get("is_electric", None),
                        is_water=requirement.get("is_water", None),
                    )
                    utility_service_response.survey_requirements.append(
                        survey_requirement
                    )

                # Return the fully populated response object
                return utility_service_response

    def ListUtilityServices(self, request, context):
        """
        Retrieves a paginated list of utility service requests with details
        such as the number of electric and water meters.

        Args:
            request: gRPC request containing pagination parameters.
            context: gRPC context for error handling and metadata.

        Returns:
            ListUtilityResponse: A response with paginated utility request data.
        """
        # Start a new database session using the context manager
        with get_db() as db_session:
            # Handle pagination logic with default values if not provided
            page = max(request.page, 1)  # Ensure page is at least 1
            page_size = max(request.page_size, 10)  # Default to 10 items per page
            offset = (page - 1) * page_size  # Calculate offset for pagination

            # Query the total number of utility service requests
            utility_query = db_session.query(UtilityServiceRequest)
            # Apply the optional search filter based on utility_number
            if request.utility_number:  # Check if utility_number is provided
                utility_query = utility_query.filter(
                    UtilityServiceRequest.utility_number.like(
                        f"%{request.utility_number}%"
                    )
                )
            total_items = utility_query.count()

            # Fetch paginated results based on the offset and limit
            utility_requests = utility_query.offset(offset).limit(page_size).all()

            # Initialize the response object with metadata
            utility_list_response = utility_request_pb2.ListUtilityResponse(
                total_count=total_items, page=page, page_size=page_size
            )

            # Loop through each utility request to fetch associated
            # meter counts and gateway counts
            for utility_request in utility_requests:
                # Get the number of Gateways mapped with this Utility Number
                gateway_count_query = text(
                    f"SELECT * from "
                    f"{SCHEMA}.get_gateway_count_by_utility(:utility_number)"
                )
                # Prepare SQL queries to get electric and water meter counts
                meter_count_query = text(
                    f"SELECT * FROM {SCHEMA}.fn_get_meter_count(:utility_number, :type)"
                )

                # Execute the query for getting the Gateway Count
                gateway_result = db_session.execute(
                    gateway_count_query,
                    {"utility_number": str(utility_request.utility_number)},
                )
                # Execute the queries for electric and water meters
                electric_result = db_session.execute(
                    meter_count_query,
                    {
                        "utility_number": str(utility_request.utility_number),
                        "type": "E",
                    },
                )
                water_result = db_session.execute(
                    meter_count_query,
                    {
                        "utility_number": str(utility_request.utility_number),
                        "type": "W",
                    },
                )

                # Fetch the results and handle null values gracefully
                electric_meter_count = electric_result.scalar() or 0
                water_meter_count = water_result.scalar() or 0
                gateway_count = gateway_result.scalar() or 0

                # Build the response object for each utility request
                utility_data = utility_request_pb2.UtilityRequest(
                    utility_request_slug=str(utility_request.slug),
                    utility_number=utility_request.utility_number,
                    account_number=utility_request.account_number,
                    region="ADDC",
                    no_electric_meter=electric_meter_count,
                    no_water_meter=water_meter_count,
                    no_of_gateways=gateway_count,
                    status=utility_request.status_relation.value,
                )

                # Add the utility data to the response list
                utility_list_response.utility_request.append(utility_data)

            # Return the fully populated response object
            return utility_list_response
