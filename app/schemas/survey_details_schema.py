from pydantic import BaseModel, ValidationError
from typing import Optional, Dict, TypeVar, Type
from app.stubs.utility_request import utility_request_pb2

T = TypeVar("T", bound=BaseModel)


class SurveyDetails(BaseModel):
    survey_slug: str
    surveyor: str
    comments: Optional[str] = None
    survey_date: str  # Expecting ISO format

    @classmethod
    def get_response(cls: Type[T], data: Dict) -> "SurveyDetails":
        print(data)
        return cls(**data)  # type: ignore[return-value]

    @classmethod
    def from_dict(
        cls: Type[T], data: Dict
    ) -> utility_request_pb2.SurveyDetails:  # type: ignore[name-defined]
        """Map a dictionary to a Pydantic model and return
        a gRPC SurveyDetails object."""
        try:
            # Validate the input data using Pydantic
            survey_details = cls(**data)

            # Convert to gRPC SurveyDetails object using individual fields
            return utility_request_pb2.SurveyDetails(  # type: ignore[attr-defined]
                survey_slug=survey_details.survey_slug,  # type: ignore[attr-defined]
                surveyor=survey_details.surveyor,  # type: ignore[attr-defined]
                comments=survey_details.comments,  # type: ignore[attr-defined]
                survey_date=survey_details.survey_date,  # type: ignore[attr-defined]
            )
        except ValidationError as e:
            print(f"Validation error: {e}")
            raise
