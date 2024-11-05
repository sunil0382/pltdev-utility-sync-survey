import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterManufacturer(Base):
    __tablename__ = "meter_manufacturer"
    __table_args__ = {"schema": SCHEMA}

    meter_manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name = Column(String(150), nullable=False)
    slug = Column(String(150), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    meter_models = relationship("MeterModel", back_populates="meter_manufacturer")
    meters = relationship("Meter", back_populates="manufacturer_relation")
