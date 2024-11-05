from sqlalchemy import Column, Boolean, BigInteger, TIMESTAMP, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class NBIoTCoverage(Base):
    __tablename__ = "nb_iot_coverage"
    __table_args__ = ({"schema": SCHEMA},)

    nb_iot_coverage_id = Column(BigInteger, primary_key=True, autoincrement=True)
    rsrp_within_acceptable_range = Column(Boolean, nullable=True)
    rsrp_value = Column(String(50), nullable=True, default=None)
    sinr_within_acceptable_range = Column(Boolean, nullable=False)
    sinr_value = Column(String(50), nullable=True, default=None)
    signal_strength_3g4g_within_range = Column(Boolean, nullable=False)
    signal_strength_3g4g_value = Column(String(50), nullable=True, default=None)
    serving_site_id = Column(String(50), nullable=True, default=None)
    serving_cell_id = Column(String(50), nullable=True, default=None)
    nb_iot_coverage_id_survey_id = Column(
        BigInteger, ForeignKey(f"{SCHEMA}.survey.survey_id"), nullable=False
    )
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now()")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now()")
    survey = relationship("Survey", back_populates="nb_iot_coverage")
