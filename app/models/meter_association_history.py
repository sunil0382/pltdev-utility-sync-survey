from sqlalchemy import Column, BigInteger, String, TIMESTAMP, text, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterAssociationHistory(Base):
    __tablename__ = "meter_association_history"
    __table_args__ = {"schema": SCHEMA}

    meter_association_history_id = Column(
        BigInteger, primary_key=True, autoincrement=True, unique=True
    )
    meter_association_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.meter_association.meter_association_id"),
        nullable=False,
    )
    meter = Column(BigInteger, ForeignKey(f"{SCHEMA}.meter.meter_id"), nullable=False)
    gateway = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.gateway.gateway_id"), nullable=False
    )
    utility_request = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.utility_service_request.utility_request_id"),
        nullable=False,
    )
    slug = Column(UUID(as_uuid=True), nullable=False, unique=True)
    room_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.room.room_id"), nullable=True, default=None
    )
    is_meter_faulty = Column(Boolean, default=False)
    association_date = Column(TIMESTAMP(timezone=True), nullable=False)
    issue_type_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.meter_issue_type.issue_type_id"),
        nullable=True,
        default=None,
    )
    issue_detail_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.meter_issue_detail.issue_detail_id"),
        nullable=True,
        default=None,
    )
    operation = Column(String(50), nullable=False)
    hes_meter_status = Column(String(100), nullable=False)
    is_meter_associated = Column(Boolean, nullable=False, default=False)
    change_timestamp = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    floor_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.floor.floor_id"), nullable=True, default=None
    )
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
