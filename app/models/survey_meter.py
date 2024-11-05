from sqlalchemy import Column, Integer, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
import datetime
from app.config.settings import SCHEMA
from app.database.base import Base


class SurveyMeter(Base):
    __tablename__ = "survey_meter"
    __table_args__ = {"schema": SCHEMA}  # Add schema
    survey_meter_id = Column(Integer, primary_key=True, autoincrement=True)
    meter_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.meter.meter_id"), nullable=False
    )
    survey_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.survey.survey_id"), nullable=False
    )
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    meter_relation = relationship("Meter")
    survey_relation = relationship("Survey")
