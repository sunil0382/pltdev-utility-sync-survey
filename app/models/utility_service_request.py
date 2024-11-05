from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, Index, UUID
from sqlalchemy.orm import relationship
import uuid
import datetime
from app.config.settings import SCHEMA
from app.database.base import Base


class UtilityServiceRequest(Base):
    __tablename__ = "utility_service_request"

    utility_request_id = Column(BigInteger, primary_key=True, autoincrement=True)
    utility_number = Column(String(70), unique=True, nullable=False)
    account_number = Column(BigInteger, nullable=False)
    region = Column(String(20), nullable=False)
    status = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.status_value.status_value_id"), nullable=False
    )
    slug = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    customer = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.customer.customer_id"), nullable=False
    )
    premise = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.premise.premise_id"), nullable=False
    )
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    customer_relation = relationship(
        "Customer", back_populates="utility_service_requests"
    )
    premise_relation = relationship(
        "Premise", back_populates="utility_service_requests"
    )
    surveys = relationship("Survey", back_populates="utility_service_request_relation")

    status_relation = relationship("StatusValue")

    __table_args__ = (
        Index("idx_utility_service_request_premise", "premise"),
        Index("idx_utility_service_request_customer", "customer"),
        Index("idx_utility_service_request_status", "status"),
        {"schema": SCHEMA},
    )
