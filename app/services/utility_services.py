import grpc
from app.database.session import get_db
from app.models import UtilityServiceRequest
from app.schemas.nbiot_schema import NBIOTCoverage
from app.schemas.premise_schema import PremiseInfo
from app.schemas.ptw_schema import PTWInfo
from app.schemas.survey_details_schema import SurveyDetails
from app.schemas.survey_gateway_schema import SurveyGatewaySchema
from app.stubs.utility_request import utility_request_pb2, utility_request_pb2_grpc
from app.services.managers.survey_manager import SurveyManager
from app.services.managers.gateway_manager import GatewayManager
from app.services.managers.meter_manager import MeterManager


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
            UtilityServiceResponse: A response object containing details of
            the utility service request.
        """
        with get_db() as db_session:
            # Query the utility service request by utility number
            utility_request = (
                db_session.query(UtilityServiceRequest)
                .filter(UtilityServiceRequest.utility_number == request.utility_number)
                .first()
            )

            if utility_request is None:
                context.set_details(
                    f"Utility request with slug '{request.utility_number}' not found."
                )
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return utility_request_pb2.UtilityServiceResponse()

            # Initialize managers
            survey_manager = SurveyManager(db_session)
            # Get survey details
            results = survey_manager.get_survey_details(request.utility_number)
            if results is None:
                context.set_details("Survey details not found.")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return utility_request_pb2.UtilityServiceResponse()
            # Extract details from the survey_details
            premise_info = results.get("premise_info", {})
            nb_iot = results.get("nb_iot_coverage", {})
            requirements = results.get("requirements", {})
            ptw = results.get("ptw", {})
            survey = results.get("survey", {})
            survey_gateways = results.get("gateways", [])
            # Constructing the UtilityServiceResponse
            utility_service_response = utility_request_pb2.UtilityServiceResponse(
                account_number=utility_request.account_number,
                utility_number=utility_request.utility_number,
                status=utility_request.status_relation.value,
                survey_details=SurveyDetails.from_dict(survey),
                premise_info=PremiseInfo.from_dict(premise_info),
                nb_oit=NBIOTCoverage.from_dict(nb_iot),
                ptw_info=PTWInfo.from_dict(ptw),
                survey_gateways=[
                    SurveyGatewaySchema.from_dict(gateway)
                    for gateway in survey_gateways
                ],
                survey_requirements=survey_manager.build_survey_requirements(
                    requirements
                ),
            )

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
        with get_db() as db_session:
            page = max(request.page, 1)  # Ensure page is at least 1
            page_size = max(request.page_size, 10)  # Default to 10 items per page
            offset = (page - 1) * page_size  # Calculate offset for pagination
            # Query the total number of utility service requests
            utility_query = db_session.query(UtilityServiceRequest)
            if request.utility_number:
                utility_query = utility_query.filter(
                    UtilityServiceRequest.utility_number.like(
                        f"%{request.utility_number}%"
                    )
                )
            total_items = utility_query.count()

            # Fetch paginated results based on the offset and limit
            utility_requests = utility_query.offset(offset).limit(page_size).all()
            total_pages = (
                total_items + page_size - 1
            ) // page_size  # Calculate total pages

            # Initialize managers
            gateway_manager = GatewayManager(db_session)
            meter_manager = MeterManager(db_session)

            utility_services = []
            for utility in utility_requests:
                electric_meter_count = meter_manager.get_meter_count(
                    utility.utility_number, meter_type="E"
                )
                water_meter_count = meter_manager.get_meter_count(
                    utility.utility_number, meter_type="W"
                )
                gateway_count = gateway_manager.get_gateway_count(
                    utility.utility_number
                )
                utility_services.append(
                    utility_request_pb2.UtilityRequest(
                        utility_request_slug=str(utility.slug),
                        utility_number=utility.utility_number,
                        account_number=utility.account_number,
                        region="ADDC",
                        no_electric_meter=electric_meter_count,
                        no_water_meter=water_meter_count,
                        no_of_gateways=gateway_count,
                        status=utility.status_relation.value,
                    )
                )
            return utility_request_pb2.ListUtilityResponse(
                total_count=total_items,
                page_size=total_pages,
                page=page,
                utility_request=utility_services,
            )
