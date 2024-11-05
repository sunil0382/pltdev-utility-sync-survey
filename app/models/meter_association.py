import uuid
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Boolean,
    TIMESTAMP,
    ForeignKey,
    text,
    CheckConstraint,
    Index,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterAssociation(Base):
    __tablename__ = "meter_association"
    __table_args__ = (
        CheckConstraint(
            "((is_meter_faulty = true AND issue_type_id IS NOT NULL) "
            "OR is_meter_faulty = false)",
            name="chk_faulty_issue_details",
        ),
        Index("idx_meter_association_floor", "floor_id"),
        Index("idx_meter_association_gateway", "gateway_id"),
        Index("idx_meter_association_history_slug", "slug"),
        Index("idx_meter_association_meter", "is_meter_faulty"),
        Index("idx_meter_association_room_id", "room_id"),
        Index("idx_meter_association_slug", "slug"),
        Index("idx_meter_association_status", "is_meter_faulty"),
        Index("idx_meter_association_utility_request", "utility_request_id"),
        {"schema": SCHEMA},
    )

    meter_association_id = Column(
        BigInteger, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    floor_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.floor.floor_id"), nullable=True, default=None
    )
    meter_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.meter.meter_id"), nullable=False
    )
    gateway_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.gateway.gateway_id"),
        nullable=True,
        default=None,
    )

    utility_request_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.utility_service_request.utility_request_id"),
        nullable=False,
    )
    slug = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    room_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.room.room_id"), nullable=True, default=None
    )
    is_meter_faulty = Column(Boolean, default=False)
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
    association_date = Column(TIMESTAMP(timezone=True), nullable=True)
    hes_meter_status = Column(String(50), nullable=True)
    is_meter_associated = Column(Boolean, nullable=False, default=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )

    floor = relationship("Floor")
    meter = relationship("Meter")
    gateway = relationship("Gateway")
    issue_type = relationship("MeterIssueType")
    issue_detail = relationship("MeterIssueDetail")
    utility_request = relationship("UtilityServiceRequest")
    room = relationship("Room")

    def __repr__(self):
        return (
            f"<MeterAssociation(utility_request_id={self.utility_request_id}, "
            f"floor_id={self.floor_id}, meter_id={self.meter_id}, "
            f"is_meter_faulty={self.is_meter_faulty}, "
            f"issue_type_id={self.issue_type_id}, "
            f"issue_detail_id={self.issue_detail_id}, "
            f"room_id={self.room_id}, gateway_id={self.gateway_id})>"
        )
