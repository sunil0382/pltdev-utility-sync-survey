import datetime

from sqlalchemy import Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterModel(Base):
    __tablename__ = "meter_model"
    __table_args__ = {"schema": SCHEMA}  # Add schema

    meter_model_id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(150), nullable=False)
    model_description = Column(String(250), nullable=True)
    brand = Column(String(75), nullable=True)
    meter_manufacturer_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.meter_manufacturer.meter_manufacturer_id"),
        nullable=False,
    )
    slug = Column(String(150), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    meter_manufacturer = relationship(
        "MeterManufacturer", back_populates="meter_models"
    )
    meters = relationship("Meter", back_populates="model_relation")
