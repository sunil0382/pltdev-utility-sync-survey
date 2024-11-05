from sqlalchemy import text
from app.config.settings import SCHEMA


class GatewayManager:
    """
    Manages operations related to utility service gateways.

    Attributes:
        db_session: The active database session for executing queries.
    """

    def __init__(self, db_session):
        """
        Initializes the GatewayManager with a database session.

        Args:
            db_session: The active database session to interact with the database.
        """
        self.db_session = db_session

    def get_gateway_count(self, utility_number):
        """
        Retrieves the count of gateways associated with a given utility number.

        Args:
            utility_number (str): The utility number to look up gateway count for.

        Returns:
            int: The count of gateways or 0 if none are found.
        """
        query = text(
            f"SELECT * FROM {SCHEMA}.get_gateway_count_by_utility(:utility_number)"
        )
        result = self.db_session.execute(query, {"utility_number": utility_number})
        return result.scalar() or 0
