import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.config.settings import SCHEMA
from app.database.base import Base


class PremiseType(Base):
    __tablename__ = "premise_type"
    __table_args__ = ({"schema": SCHEMA},)

    premise_type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    __table_args__ = {"schema": SCHEMA}  # type: ignore[assignment]
