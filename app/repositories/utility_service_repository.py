from sqlalchemy import text
from app.models import UtilityServiceRequest
from app.config.settings import SCHEMA


class UtilityServiceRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def fetch_utility_request(self, utility_number):
        return (
            self.db_session.query(UtilityServiceRequest)
            .filter(UtilityServiceRequest.utility_number == utility_number)
            .first()
        )

    def get_survey_details(self, utility_number):
        utility_request_query = text(
            f"SELECT * from {SCHEMA}.fn_get_survey_by_utility_number(:utility_number)"
        )
        result = self.db_session.execute(
            utility_request_query, {"utility_number": utility_number}
        )
        return result.fetchone()

    def get_gateway_count(self, utility_number):
        gateway_count_query = text(
            f"SELECT * from {SCHEMA}.get_gateway_count_by_utility(:utility_number)"
        )
        result = self.db_session.execute(
            gateway_count_query, {"utility_number": utility_number}
        )
        return result.scalar() or 0

    def get_meter_count(self, utility_number, meter_type):
        meter_count_query = text(
            f"SELECT * FROM {SCHEMA}.fn_get_meter_count(:utility_number, :type)"
        )
        result = self.db_session.execute(
            meter_count_query, {"utility_number": utility_number, "type": meter_type}
        )
        return result.scalar() or 0
