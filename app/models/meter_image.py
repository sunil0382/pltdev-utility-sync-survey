import uuid
from sqlalchemy import Column, ForeignKey, BigInteger, Text, UUID, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterImage(Base):
    __tablename__ = "meter_image"
    __table_args__ = {"schema": SCHEMA}

    meter_image_id = Column(BigInteger, primary_key=True, autoincrement=True)
    meter_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.meter.meter_id", ondelete="CASCADE"),
        nullable=False,
    )
    image_url = Column(Text, nullable=False)
    slug = Column(UUID, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    meter = relationship("Meter", back_populates="images")
