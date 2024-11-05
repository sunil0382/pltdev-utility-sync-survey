from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    BigInteger,
    ForeignKey,
    Index,
    UUID,
    Text,
)
from sqlalchemy.orm import relationship
import uuid
import datetime
from app.config.settings import SCHEMA
from app.database.base import Base


class Survey(Base):
    __tablename__ = "survey"

    survey_id = Column(Integer, primary_key=True, autoincrement=True)
    surveyor = Column(String(150), nullable=False)
    survey_date = Column(DateTime(timezone=True), nullable=False)
    slug = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    utility_service_request = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.utility_service_request.utility_request_id"),
        nullable=False,
    )
    premise_id = Column(BigInteger, ForeignKey(f"{SCHEMA}.premise.premise_id"))
    status_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.status_value.status_value_id"), nullable=True
    )
    comments = Column(Text)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    premise_relation = relationship("Premise")
    utility_service_request_relation = relationship(
        "UtilityServiceRequest", back_populates="surveys"
    )
    ptw_information = relationship("PTWInformation", back_populates="survey")
    nb_iot_coverage = relationship("NBIoTCoverage", back_populates="survey")
    status_value = relationship("StatusValue", back_populates="surveys")
    requirements = relationship("SurveyRequirement", back_populates="survey")

    __table_args__ = (
        Index("idx_survey_utility_service_request", "utility_service_request"),
        Index("idx_survey_premise_id", "premise_id"),
        {"schema": SCHEMA},
    )
