from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from services.utility_request_service import (
    list_utility_requests,
    fetch_utility_request,
)

router = APIRouter(prefix="/utility_requests")


@router.get("/", response_class=JSONResponse)
def get_utility_requests(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Number of requests per page"),
    utility_number: str = Query(None, description="Search with Utility Number"),
):
    return list_utility_requests(page, page_size, utility_number)


@router.get("/{utility_number}", response_class=JSONResponse)
def get_utility_request(utility_number: str):
    """
    Retrieve a utility service request by its utility number.
    """
    response = fetch_utility_request(utility_number)
    # If `fetch_utility_request` returns a response object, extract JSON content
    if response.status_code != 200:
        return response

    # Properly return the JSON content of the response
    return response
