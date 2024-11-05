from sqlalchemy import (
    BigInteger,
    UniqueConstraint,
    Column,
    CHAR,
    String,
    ForeignKey,
    Numeric,
    Boolean,
    DateTime,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.config.settings import SCHEMA
from app.database.base import Base


class SurveyGateway(Base):
    __tablename__ = "survey_gateway"
    __table_args__ = (
        UniqueConstraint("slug", name="survey_gateway_slug_key"),
        {"schema": SCHEMA},
    )

    survey_gateway_id = Column(BigInteger, primary_key=True, autoincrement=True)
    gateway_type = Column(CHAR(1), nullable=False, default="H")
    gateway_connection_type_id = Column(
        BigInteger,
        ForeignKey(
            f"{SCHEMA}.gateway_connection_type.gateway_connection_type_id",
            ondelete="SET NULL",
        ),
        nullable=False,
    )
    gateway_model_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.gateway_model.gateway_model_id", ondelete="SET NULL"),
        nullable=False,
    )
    gateway_scenario = Column(String(10))
    cable_length = Column(Numeric(8, 2))
    room_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.room.room_id", ondelete="SET NULL"),
        nullable=False,
    )
    floor_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.floor.floor_id", ondelete="SET NULL"),
        nullable=False,
    )
    power_interruption = Column(Boolean, default=False)
    signal_strength = Column(Numeric(8, 2))
    antenna = Column(Boolean, default=False)
    label = Column(String(150))
    survey_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.survey.survey_id", ondelete="SET NULL"),
        nullable=False,
    )
    slug = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )
    # Relationships (if needed)
    gateway_connection_type = relationship("GatewayConnectionType")
    gateway_model = relationship("GatewayModel")
    room = relationship("Room")
    floor = relationship("Floor")
    survey = relationship("Survey")
