import uuid
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class SurveyRequirement(Base):
    __tablename__ = "survey_requirement"
    __table_args__ = {"schema": SCHEMA}

    survey_requirement_id = Column(Integer, primary_key=True, autoincrement=True)
    survey_requirement_survey_id = Column(
        Integer, ForeignKey(f"{SCHEMA}.survey.survey_id"), nullable=False
    )
    requirement_key = Column(String(100), nullable=False)
    is_electric = Column(Boolean, nullable=False, default=False)
    is_water = Column(Boolean, nullable=False, default=False)
    slug = Column(UUID, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now()")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now()")

    survey = relationship("Survey", back_populates="requirements")
