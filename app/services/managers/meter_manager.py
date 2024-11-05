from sqlalchemy import text
from app.config.settings import SCHEMA


class MeterManager:
    """
    Manages operations related to utility service meters.

    Attributes:
        db_session: The active database session for executing queries.
    """

    def __init__(self, db_session):
        """
        Initializes the MeterManager with a database session.

        Args:
            db_session: The active database session to interact with the database.
        """
        self.db_session = db_session

    def get_meter_count(self, utility_number, meter_type):
        """
        Retrieves the count of meters (electric or water) for a given utility number.

        Args:
            utility_number (str): The utility number to look up meter count for.
            meter_type (str): The type of meter ('E' for electric, 'W' for water).

        Returns:
            int: The count of meters or 0 if none are found.
        """
        query = text(
            f"SELECT * FROM {SCHEMA}.fn_get_meter_count(:utility_number, :type)"
        )
        result = self.db_session.execute(
            query, {"utility_number": utility_number, "type": meter_type}
        )
        return result.scalar() or 0
