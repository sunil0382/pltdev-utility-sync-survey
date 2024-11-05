from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index, BigInteger
from sqlalchemy.orm import relationship
import datetime
from app.config.settings import SCHEMA
from app.database.base import Base


class StatusValue(Base):
    __tablename__ = "status_value"

    status_value_id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(100), nullable=False)
    status_category = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.status_category.status_category_id"),
        nullable=False,
    )
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    status_category_relation = relationship(
        "StatusCategory", back_populates="status_values"
    )
    surveys = relationship("Survey", back_populates="status_value")
    utility_service_requests = relationship(
        "UtilityServiceRequest", back_populates="status_relation"
    )

    __table_args__ = (
        Index("idx_status_value_status_category", "status_category"),
        {"schema": SCHEMA},
    )
