from pydantic import BaseModel, Field
from typing import Optional, TypeVar
from uuid import UUID
from decimal import Decimal
from app.stubs.survey_gateways import survey_gateways_pb2

T = TypeVar("T", bound=BaseModel)


class SurveyGatewaySchema(BaseModel):
    gateway_type: str = Field(
        ..., max_length=1, description="Type of gateway (e.g., 'H')."
    )
    connection_type: str
    model_name: Optional[str] = None
    gateway_scenario: Optional[str] = Field(None, max_length=10)
    cable_length: Optional[Decimal] = None
    room: Optional[str] = None
    floor_code: Optional[str] = None
    floor_id: Optional[int] = None
    power_interruption: bool = False
    signal_strength: Optional[Decimal] = None
    antenna: bool = False
    label: Optional[str] = Field(None, max_length=150)
    slug: str

    @classmethod
    def get_response(cls, data: dict) -> "SurveyGatewaySchema":
        return cls(**data)

    @classmethod
    def from_protobuf(
        cls, gw: survey_gateways_pb2.SurveyGateways  # type: ignore[name-defined]
    ) -> "SurveyGatewaySchema":  # type: ignore[name-defined]
        """Converts a SurveyGateways protobuf object to a SurveyGatewaySchema."""
        return cls(
            gateway_type=gw.gateway_type,
            connection_type=gw.connection_type,
            model_name=gw.model_name,
            gateway_scenario=gw.gateway_scenario,
            cable_length=Decimal(gw.cable_length) if gw.cable_length else None,
            room=gw.room,
            floor_code=gw.floor_code,
            floor_id=gw.floor_id,
            power_interruption=gw.power_interruption,
            signal_strength=Decimal(gw.signal_strength) if gw.signal_strength else None,
            antenna=gw.antenna,
            label=gw.label,
            slug=str(gw.slug),
        )

    @classmethod
    def from_dict(
        cls, data: dict
    ) -> survey_gateways_pb2.SurveyGateways:  # type: ignore[name-defined]
        """Converts a dictionary to a SurveyGateways protobuf object."""
        return survey_gateways_pb2.SurveyGateways(  # type: ignore[attr-defined]
            gateway_type=data.get("gateway_type"),
            connection_type=data.get("connection_type"),
            model_name=data.get("model_name"),
            gateway_scenario=data.get("gateway_scenario"),
            cable_length=(
                float(data["cable_length"]) if data.get("cable_length") else None
            ),
            room=data.get("room"),
            floor_code=data.get("floor_code"),
            floor_id=data.get("floor_id"),
            power_interruption=data.get("power_interruption", False),
            signal_strength=(
                float(data["signal_strength"]) if data.get("signal_strength") else None
            ),
            antenna=data.get("antenna", False),
            label=data.get("label"),
            slug=str(data.get("slug")),
        )

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
