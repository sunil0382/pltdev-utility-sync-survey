from sqlalchemy import (
    Column,
    BigInteger,
    Numeric,
    String,
    ForeignKey,
    DateTime,
    Index,
    UUID,
    Integer,
)
from sqlalchemy.orm import relationship
import uuid
import datetime
from app.config.settings import SCHEMA
from app.database.base import Base


class Premise(Base):
    __tablename__ = "premise"
    __table_args__ = ({"schema": SCHEMA},)

    premise_id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Numeric(15, 10))
    longitude = Column(Numeric(15, 10))
    building_name = Column(String(150))
    building_number = Column(String(100), nullable=False)
    plot_number = Column(String(100))
    address = Column(String(400))
    district = Column(String(100))
    street = Column(String(100))
    city = Column(String(50))
    plot = Column(String(250))
    slug = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    premise_type = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.premise_type.premise_type_id"), nullable=False
    )
    emirate_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.emirate.emirate_id"), nullable=False
    )
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    premise_type_relation = relationship("PremiseType")
    # surveys_from_premise = relationship('Survey', backref='premise_relation')
    emirate_relation = relationship("Emirate")
    utility_service_requests = relationship("UtilityServiceRequest")

    __table_args__ = (  # type: ignore[assignment]
        Index("idx_premise_premise_type", "premise_type"),
        Index("idx_premise_emirate_id", "emirate_id"),
        {"schema": SCHEMA},
    )
