from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import relationship
import datetime
from app.config.settings import SCHEMA
from app.database.base import Base


class SurveyAttribute(Base):
    __tablename__ = "survey_attribute"
    __table_args__ = {"schema": SCHEMA}  # Add schema

    survey_attribute_id = Column(Integer, primary_key=True, autoincrement=True)
    attribute_name = Column(String(100), nullable=False)
    attribute_value = Column(String(100), nullable=False)
    survey_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.survey.survey_id"), nullable=False
    )
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    survey_relation = relationship("Survey")
