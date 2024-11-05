from pydantic import BaseModel, ValidationError
from typing import Dict
from app.stubs.ptw import ptw_pb2


class PTWInfo(BaseModel):
    start_date: str  # Expecting ISO format
    end_date: str  # Expecting ISO format
    slug: str

    @classmethod
    def from_dict(cls, data: Dict) -> ptw_pb2.PTWInfo:  # type: ignore[name-defined]
        """Convert a dictionary to a validated Pydantic model and
        return a gRPC PTWInfo object."""
        try:
            # Validate the input data with the Pydantic model
            model = cls(**data)

            # Convert the Pydantic model to a gRPC PTWInfo object
            return ptw_pb2.PTWInfo(  # type: ignore[attr-defined]
                start_date=model.start_date,
                end_date=model.end_date,
                slug=model.slug,
            )
        except ValidationError as e:
            print(f"Validation error: {e}")
            raise
