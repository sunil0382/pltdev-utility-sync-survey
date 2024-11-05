import grpc
from fastapi import status
from fastapi.responses import JSONResponse
from app.schemas.nbiot_schema import NBIOTCoverage
from app.schemas.premise_schema import PremiseInfo
from app.schemas.survey_gateway_schema import SurveyGatewaySchema
from app.stubs.utility_request import utility_request_pb2, utility_request_pb2_grpc


def create_response(
    data=None, message="Success", code=200, status_code=status.HTTP_200_OK
):
    return JSONResponse(
        status_code=status_code,
        content={"code": code, "message": message, "data": data},
    )


# Helper function to get the gRPC client for UtilityRequest service
def get_utility_request_grpc_client():
    channel = grpc.insecure_channel("localhost:50051")
    stub = utility_request_pb2_grpc.UtilityServicesStub(channel)
    return stub


# List Utility Requests API
def list_utility_requests(
    page: int = 1,
    page_size: int = 10,
    utility_number: str = None,  # type: ignore[assignment]
):
    stub = get_utility_request_grpc_client()
    try:
        grpc_response = stub.ListUtilityServices(  # type: ignore[attr-defined]
            utility_request_pb2.ListUtilityRequest(  # type: ignore[attr-defined]
                page=page, page_size=page_size, utility_number=utility_number
            )
        )
        requests = [
            {
                "utility_request_slug": req.utility_request_slug,
                "utility_number": req.utility_number,
                "account_number": req.account_number,
                "region": req.region,
                "no_electric_meter": req.no_electric_meter,
                "no_water_meter": req.no_water_meter,
                "no_of_gateways": req.no_of_gateways,
                "status": req.status,
            }
            for req in grpc_response.utility_request
        ]

        pagination_info = {
            "total_count": grpc_response.total_count,
            "page": page,
            "page_size": page_size,
        }

        return create_response(
            data={"pagination_info": pagination_info, "utility_requests": requests},
            message="Utility requests fetched successfully",
            code=200,
        )

    except grpc.RpcError:

        return create_response(
            message="Failed to fetch utility requests",
            code=500,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# Fetch Utility Request API based on utility_number
def fetch_utility_request(utility_number: str):
    stub = get_utility_request_grpc_client()

    try:
        print(f"Sending request with utility_number: {utility_number}")
        grpc_response = stub.FetchUtilityRequest(
            utility_request_pb2.UtilityServiceRequest(  # type: ignore[attr-defined]
                utility_number=utility_number
            )
        )

        if grpc_response.utility_number == "":
            return create_response(
                message=f"Utility request with utility number "
                f"'{utility_number}' not found.",
                code=404,
                data={},
                status_code=status.HTTP_404_NOT_FOUND,
            )
        # Prepare the response data
        survey_gateways = [
            SurveyGatewaySchema.from_protobuf(gw)
            for gw in grpc_response.survey_gateways
        ]

        # Convert survey_gateways to a list of dictionaries
        survey_gateways_dict = [gw.dict() for gw in survey_gateways]
        survey_requirements = [
            {
                "slug": req.slug,
                "requirement_key": req.requirement_key,
                "is_water": req.is_water,
                "is_electric": req.is_electric,
            }
            for req in grpc_response.survey_requirements
        ]

        utility_request_data = {
            "status": grpc_response.status,
            "utility_number": grpc_response.utility_number,
            "account_number": grpc_response.account_number,
            "region": "ADDC",
            "survey_details": {
                "survey_slug": grpc_response.survey_details.survey_slug,
                "surveyor": grpc_response.survey_details.surveyor,
                "comments": grpc_response.survey_details.comments,
                "survey_date": grpc_response.survey_details.survey_date,
            },
            "premise_info": PremiseInfo.get_response(grpc_response.premise_info),
            "nb_oit": NBIOTCoverage.get_response(grpc_response.nb_oit),
            "survey_requirements": survey_requirements,
            "survey_gateways": survey_gateways_dict,
            "ptw": {
                "start_date": grpc_response.ptw_info.start_date,
                "end_date": grpc_response.ptw_info.end_date,
                "slug": grpc_response.ptw_info.slug,
            },
        }

        return create_response(
            data=utility_request_data,
            message="Utility request fetched successfully",
            code=200,
        )

    except grpc.RpcError as e:
        print(f"gRPC error occurred: {e.code()}, {e.details()}")
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return create_response(
                message=f"Utility request with utility number "
                f"'{utility_number}' not found.",
                code=404,
                status_code=status.HTTP_404_NOT_FOUND,
            )

        return create_response(
            message="Failed to fetch utility request",
            code=500,
            data={},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
