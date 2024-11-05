from sqlalchemy import text
from app.config.settings import SCHEMA
from app.stubs.survey_requirements import survey_requirements_pb2


class SurveyManager:
    """
    Manages survey-related operations, including retrieving survey details
    and building survey requirements.

    Attributes:
        db_session: The active database session for executing queries.
    """

    def __init__(self, db_session):
        """
        Initializes the SurveyManager with a database session.

        Args:
            db_session: The active database session to interact with the database.
        """
        self.db_session = db_session

    def get_survey_details(self, utility_number):
        """
        Retrieves survey details based on a given utility number.

        Args:
            utility_number (str): The utility number to look up survey details for.

        Returns:
            dict: A dictionary containing flattened survey details or
            None if no details are found.
        """
        query = text(
            f"SELECT * FROM {SCHEMA}.fn_get_survey_by_utility_number(:utility_number)"
        )
        result = self.db_session.execute(query, {"utility_number": utility_number})
        row = result.fetchone()

        if row:
            # Unpack row and flatten survey details at the root level
            survey_details = row.survey_details if row.survey_details else {}

            survey_data = {
                "utility_number": row.utility_number,
                "account_number": row.account_number,
                "region": row.region,
                "status": row.status,
                "survey": {
                    "survey_slug": survey_details.get("survey_slug", ""),
                    "surveyor": survey_details.get("surveyor", ""),
                    "survey_date": survey_details.get("survey_date", ""),
                    "comments": survey_details.get("comments", ""),
                },
                "premise_info": survey_details.get("premise_info", {}),
                "nb_iot_coverage": survey_details.get("nb_iot_coverage", {}),
                "requirements": survey_details.get("requirements", []),
                "ptw": survey_details.get("ptw", {}),
                "gateways": survey_details.get("gateways", []),
            }
            return survey_data

        # Return None if no result is found
        return None

    def build_survey_requirements(self, requirements):
        """
        Constructs survey requirement objects from a list of requirements.

        Args:
            requirements (list): A list of requirements dictionaries.

        Returns:
            list: A list of SurveyRequirements protobuf objects.
        """
        survey_requirements = []
        for requirement in requirements:
            survey_requirement = survey_requirements_pb2.SurveyRequirements(
                slug=str(requirement.get("survey_requirement_slug", "")),
                requirement_key=requirement.get("requirement_key", None),
                is_electric=requirement.get("is_electric", None),
                is_water=requirement.get("is_water", None),
            )
            survey_requirements.append(survey_requirement)
        return survey_requirements
