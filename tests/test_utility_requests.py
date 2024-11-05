from fastapi.testclient import TestClient
from fastapi import FastAPI

mock_app = FastAPI()


@mock_app.get("/utility_requests/")
async def mock_get_utility_requests(page: int = 1, page_size: int = 10):
    return {
        "code": 200,
        "message": "Utility requests fetched successfully",
        "data": {
            "pagination_info": {
                "total_count": 50,
                "page": page,
                "page_size": page_size,
            },
            "utility_requests": [
                {
                    "utility_request_slug": "UN-1000001957",
                    "utility_number": "UN-1000001957",
                    "account_number": 957,
                    "region": "ADDC",
                    "no_electric_meter": 2,
                    "no_water_meter": 1,
                    "no_of_gateways": 1,
                }
            ],
        },
    }


@mock_app.get("/utility_requests/{utility_number}")
async def mock_get_utility_request(utility_number: str):
    if utility_number == "UN-1000001957":
        return {
            "code": 200,
            "message": "Utility request fetched successfully",
            "data": {
                "utility_number": "UN-1000001957",
                "account_number": 957,
                "region": "ADDC",
                "status": "INSTALLATION PASSED PARTIALLY",
                "survey_details": {
                    "survey_slug": "6540a521-5981-4e5d-aea4-3ae5b73ae93f",
                    "surveyor": "Mujibu Rahman",
                    "comments": "",
                    "survey_date": "2022-07-26T12:43:49.317+04:00",
                },
                "premise_info": {
                    "latitude": "24.4498131328",
                    "longitude": "54.6003432470",
                    "building_name": "AL NASEEM C",
                    "building_number": "4599944511",
                    "plot_number": "RBW248",
                    "address": "AL NASEEM C",
                    "district": "Al Rahah",
                    "street": "Al Bandar St",
                    "city": "شاطئ الراحة",
                    "premise_type": "HIGH-RISE BUILDING",
                    "emirate": "ABU DHABI EASTERN REGION",
                },
                "nb_oit": {
                    "rsrp_within_acceptable_range": True,
                    "sinr_within_acceptable_range": True,
                    "signal_strength_3g4g_within_range": False,
                },
                "survey_requirements": [
                    {
                        "slug": "req1",
                        "requirement_key": "adequate_space",
                        "is_water": True,
                        "is_electric": True,
                    }
                ],
            },
        }
    else:
        return {
            "code": 404,
            "message": (
                f"Utility request with utility number '{utility_number}' " "not found."
            ),
        }


# Use the mock app for testing
client = TestClient(mock_app)


def test_get_utility_requests() -> None:
    """Test fetching utility requests with pagination."""
    response = client.get("/utility_requests/?page=1&page_size=10")

    assert response.status_code == 200
    assert response.json() == {
        "code": 200,
        "message": "Utility requests fetched successfully",
        "data": {
            "pagination_info": {"total_count": 50, "page": 1, "page_size": 10},
            "utility_requests": [
                {
                    "utility_request_slug": "UN-1000001957",
                    "utility_number": "UN-1000001957",
                    "account_number": 957,
                    "region": "ADDC",
                    "no_electric_meter": 2,
                    "no_water_meter": 1,
                    "no_of_gateways": 1,
                }
            ],
        },
    }


def test_get_utility_request_found():
    """Test retrieving a valid utility request."""
    response = client.get("/utility_requests/UN-1000001957")

    assert response.status_code == 200
    assert response.json() == {
        "code": 200,
        "message": "Utility request fetched successfully",
        "data": {
            "utility_number": "UN-1000001957",
            "account_number": 957,
            "region": "ADDC",
            "status": "INSTALLATION PASSED PARTIALLY",
            "survey_details": {
                "survey_slug": "6540a521-5981-4e5d-aea4-3ae5b73ae93f",
                "surveyor": "Mujibu Rahman",
                "comments": "",
                "survey_date": "2022-07-26T12:43:49.317+04:00",
            },
            "premise_info": {
                "latitude": "24.4498131328",
                "longitude": "54.6003432470",
                "building_name": "AL NASEEM C",
                "building_number": "4599944511",
                "plot_number": "RBW248",
                "address": "AL NASEEM C",
                "district": "Al Rahah",
                "street": "Al Bandar St",
                "city": "شاطئ الراحة",
                "premise_type": "HIGH-RISE BUILDING",
                "emirate": "ABU DHABI EASTERN REGION",
            },
            "nb_oit": {
                "rsrp_within_acceptable_range": True,
                "sinr_within_acceptable_range": True,
                "signal_strength_3g4g_within_range": False,
            },
            "survey_requirements": [
                {
                    "slug": "req1",
                    "requirement_key": "adequate_space",
                    "is_water": True,
                    "is_electric": True,
                }
            ],
        },
    }


def test_get_utility_request_not_found():
    """Test retrieving a non-existent utility request."""
    UN = "UNAD-4464645645"
    response = client.get(f"/utility_requests/{UN}")
    assert response.json()["code"] == 404
    assert (
        response.json()["message"]
        == f"Utility request with utility number '{UN}' not found."
    )
