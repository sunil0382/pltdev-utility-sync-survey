import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterProtocol(Base):
    __tablename__ = "meter_protocol"
    __table_args__ = {"schema": SCHEMA}  # Add schema

    meter_protocol_id = Column(Integer, primary_key=True, autoincrement=True)
    protocol_name = Column(String(150), nullable=False)
    slug = Column(String(150), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    meters = relationship("Meter", back_populates="protocol_relation")
