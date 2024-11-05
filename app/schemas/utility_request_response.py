from app.schemas.nbiot_schema import NBIOTCoverage
from app.schemas.premise_schema import PremiseInfo
from app.schemas.ptw_schema import PTWInfo
from app.schemas.survey_details_schema import SurveyDetails
from pydantic import BaseModel
from typing import Dict


class UtilityServiceResponse(BaseModel):
    account_number: str
    utility_number: str
    status: str
    survey_details: SurveyDetails
    premise_info: PremiseInfo
    nb_oit: NBIOTCoverage
    ptw_info: PTWInfo


def create_response(
    account_number: str,
    utility_number: str,
    status: str,
    survey_details: Dict,
    premise_info: Dict,
    nb_oit: Dict,
    ptw: Dict,
) -> UtilityServiceResponse:
    return UtilityServiceResponse(
        account_number=account_number,
        utility_number=utility_number,
        status=status,
        survey_details=SurveyDetails(**survey_details),
        premise_info=PremiseInfo(**premise_info),
        nb_oit=NBIOTCoverage(**nb_oit),
        ptw_info=PTWInfo(**ptw),
    )
