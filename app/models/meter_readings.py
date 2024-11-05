from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    Numeric,
    String,
    TIMESTAMP,
    ForeignKey,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterReadings(Base):
    __tablename__ = "meter_readings"
    __table_args__ = {"schema": SCHEMA}

    meter_reading_id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True
    )
    meter = Column(BigInteger, ForeignKey(f"{SCHEMA}.meter.meter_id"), nullable=False)
    readings = Column(Numeric(20, 5), nullable=False)
    reading_date = Column(TIMESTAMP(timezone=True), nullable=False)
    reading_type = Column(String(10), nullable=False, server_default="B")
    reading_source = Column(String(200), nullable=False)
    slug = Column(UUID(as_uuid=True), nullable=False, unique=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
