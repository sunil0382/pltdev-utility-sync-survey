from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    BigInteger,
    UniqueConstraint,
    Boolean,
    CHAR,
    TIMESTAMP,
    func,
    Date,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.config.settings import SCHEMA
from app.database.base import Base


class Meter(Base):
    __tablename__ = "meter"

    meter_id = Column(BigInteger, primary_key=True, autoincrement=True)
    meter_serial = Column(String(150), nullable=False, unique=True)
    measuring_point = Column(String(150), nullable=False, unique=True)
    badge_number = Column(String(150), nullable=False, unique=True)
    meter_model_id = Column(
        Integer, ForeignKey(f"{SCHEMA}.meter_model.meter_model_id"), nullable=False
    )
    meter_manufacturer_id = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.meter_manufacturer.meter_manufacturer_id"),
        nullable=False,
    )
    meter_protocol_id = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.meter_protocol.meter_protocol_id"),
        nullable=False,
    )
    meter_type = Column(CHAR(1), nullable=False, default="H")
    is_p2p = Column(Boolean, nullable=False, default=False)
    is_wireless = Column(Boolean, nullable=False, default=False)
    is_mdm = Column(Boolean, nullable=False, default=False)
    slug = Column(PG_UUID(as_uuid=True), nullable=False, unique=True)
    meter_priority = Column(String(2))
    year_of_manufacture = Column(Date)
    meter_rag = Column(String(10))
    source = Column(String(200), nullable=False, default="MDM")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )

    model_relation = relationship("MeterModel", back_populates="meters")
    manufacturer_relation = relationship("MeterManufacturer", back_populates="meters")
    protocol_relation = relationship("MeterProtocol", back_populates="meters")
    images = relationship(
        "MeterImage", back_populates="meter", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("meter_serial", name="meters_meter_serial_key"),
        UniqueConstraint("measuring_point", name="meters_measuring_point_key"),
        UniqueConstraint("badge_number", name="meters_badge_number_key"),
        UniqueConstraint("slug", name="meters_slug_key"),
        {"schema": SCHEMA},
    )
