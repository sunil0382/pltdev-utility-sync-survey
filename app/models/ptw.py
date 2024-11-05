from sqlalchemy import Column, Date, Boolean, BigInteger, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class PTWInformation(Base):
    __tablename__ = "ptw_information"
    __table_args__ = ({"schema": SCHEMA},)

    ptw_information_id = Column(BigInteger, primary_key=True, autoincrement=True)
    effective_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=False)
    ptw_survey_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.survey.survey_id"), nullable=False
    )
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now()")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now()")

    survey = relationship("Survey", back_populates="ptw_information")
