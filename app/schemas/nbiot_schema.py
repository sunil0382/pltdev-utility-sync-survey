from pydantic import BaseModel, ValidationError
from typing import Dict
from decimal import Decimal
from uuid import UUID
from app.stubs.nb_iot_coverage import nb_iot_coverage_pb2


class NBIOTCoverage(BaseModel):
    rsrp_within_acceptable_range: bool
    rsrp_value: str
    sinr_within_acceptable_range: bool
    sinr_value: str
    signal_strength_3g4g_within_range: bool
    signal_strength_3g4g_value: str
    serving_site_id: str
    serving_cell_id: str
    slug: str

    @classmethod
    def from_dict(
            cls, data: Dict
    ) -> nb_iot_coverage_pb2.NBIOTCoverage:  # type: ignore[name-defined]
        """Convert a dictionary to a validated Pydantic model and return
        a gRPC NBIOTCoverage object."""
        try:
            # Validate and parse the input data using the Pydantic model
            model = cls(**data)
            signal_strength = model.signal_strength_3g4g_within_range
            # Convert the Pydantic model to a gRPC NBIOTCoverage object
            return nb_iot_coverage_pb2.NBIOTCoverage(  # type: ignore[attr-defined]
                rsrp_within_acceptable_range=model.rsrp_within_acceptable_range,
                rsrp_value=model.rsrp_value,
                sinr_within_acceptable_range=model.sinr_within_acceptable_range,
                sinr_value=model.sinr_value,
                signal_strength_3g4g_within_range=signal_strength,
                signal_strength_3g4g_value=model.signal_strength_3g4g_value,
                serving_site_id=model.serving_site_id,
                serving_cell_id=model.serving_cell_id,
                slug=model.slug,
            )
        except ValidationError as e:
            print(f"Validation error: {e}")
            raise

    # mypy: ignore-errors
    @classmethod
    def get_response(
            cls, data: nb_iot_coverage_pb2.NBIOTCoverage) -> Dict:  # type: ignore
        """Creates a NBIOTCoverage instance from a gRPC response object and
        returns it as a dictionary."""
        return {
            "rsrp_within_acceptable_range": data.rsrp_within_acceptable_range,
            "rsrp_value": data.rsrp_value,
            "sinr_within_acceptable_range": data.sinr_within_acceptable_range,
            "sinr_value": data.sinr_value,
            "signal_strength_3g4g_within_range": data.signal_strength_3g4g_within_range,
            "signal_strength_3g4g_value": data.signal_strength_3g4g_value,
            "serving_site_id": data.serving_site_id,
            "serving_cell_id": data.serving_cell_id,
            "slug": data.slug,
        }

    def dict(self, **kwargs):
        """Override dict method to convert Decimal and
        UUID to JSON-serializable formats."""
        original_dict = super().dict(**kwargs)
        return {
            k: (
                float(v)
                if isinstance(v, Decimal)
                else str(v) if isinstance(v, UUID) else v
            )
            for k, v in original_dict.items()
        }
