from sqlalchemy import Column, Integer, String, TIMESTAMP
from app.config.settings import SCHEMA
from app.database.base import Base


class Emirate(Base):
    __tablename__ = "emirate"
    __table_args__ = {"schema": SCHEMA}

    emirate_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now")
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default="now", onupdate="now"
    )
