from pydantic import BaseModel, ValidationError
from typing import Dict
from decimal import Decimal
from uuid import UUID

from app.stubs.utility_request import premise_info_pb2


class PremiseInfo(BaseModel):
    latitude: str
    longitude: str
    building_name: str
    building_number: str
    plot_number: str
    address: str
    district: str
    street: str
    city: str
    plot: str
    slug: str
    premise_type: str
    emirate: str

    @classmethod
    def from_dict(
        cls, data: Dict
    ) -> premise_info_pb2.PremiseInfo:  # type: ignore[name-defined]
        """Convert a dictionary to a validated Pydantic model and return
        a gRPC PremiseInfo object."""
        try:
            # Validate and parse the input data
            model = cls(**data)

            # Convert to gRPC PremiseInfo object
            return premise_info_pb2.PremiseInfo(  # type: ignore[attr-defined]
                latitude=model.latitude,
                longitude=model.longitude,
                building_name=model.building_name,
                building_number=model.building_number,
                plot_number=model.plot_number,
                address=model.address,
                district=model.district,
                street=model.street,
                city=model.city,
                plot=model.plot,
                slug=model.slug,
                premise_type=model.premise_type,
                emirate=model.emirate,
            )
        except ValidationError as e:
            print(f"Validation error: {e}")
            raise

    def dict(self, **kwargs):
        """Override dict method to convert Decimal and UUID
        to JSON-serializable formats."""
        original_dict = super().dict(**kwargs)
        return {
            k: (
                float(v)
                if isinstance(v, Decimal)
                else str(v) if isinstance(v, UUID) else v
            )
            for k, v in original_dict.items()
        }

    # mypy: ignore-errors
    @classmethod
    def get_response(cls, data: premise_info_pb2.PremiseInfo) -> Dict:  # type: ignore
        """Creates a PremiseInfo instance from a gRPC response
        object and returns it as a dictionary."""
        return {
            "latitude": data.latitude,
            "longitude": data.longitude,
            "building_name": data.building_name,
            "building_number": data.building_number,
            "plot_number": data.plot_number,
            "address": data.address,
            "district": data.district,
            "street": data.street,
            "city": data.city,
            "plot": data.plot,
            "slug": data.slug,
            "premise_type": data.premise_type,
            "emirate": data.emirate,
        }
