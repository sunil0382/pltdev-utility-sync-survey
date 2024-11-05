from sqlalchemy import Column, Integer, String, DateTime, UUID
import uuid
import datetime
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {"schema": SCHEMA}  # Add schema

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name_en = Column(String(250))
    first_name_ar = Column(String(250))
    last_name_en = Column(String(250))
    last_name_ar = Column(String(250))
    primary_contact_number = Column(String(150), nullable=False)
    secondary_contact_number = Column(String(150))
    email = Column(String(100))
    slug = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    utility_service_requests = relationship(
        "UtilityServiceRequest", back_populates="customer_relation"
    )
