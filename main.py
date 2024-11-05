from app.config.settings import settings
from app.config.settings import SCHEMA
from app.schemas.utility_service_request_schema import UtilityServiceRequestSchema

print(settings.ADDC_SCHEMA)
print(SCHEMA)

data = {
    "utility_number": "UNAD-00000000212240",
    "account_number": 1234567890,
    "region": "East",
    "status": 2,
    "slug": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "customer": {"customer_name": "Sajeesh", "phone": "9995889898"},
    "premise": 2001,
}

utility_service_request = UtilityServiceRequestSchema(**data)  # type: ignore[arg-type]
print(utility_service_request.json())
