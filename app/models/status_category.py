import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.config.settings import SCHEMA
from app.database.base import Base


class StatusCategory(Base):
    __tablename__ = "status_category"
    __table_args__ = {"schema": SCHEMA}  # Add schema

    status_category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    status_values = relationship(
        "StatusValue", back_populates="status_category_relation"
    )
