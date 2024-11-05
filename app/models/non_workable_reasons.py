from sqlalchemy import Column, Integer, String
from app.config.settings import SCHEMA
from app.database.base import Base


class NonWorkableReasons(Base):
    __tablename__ = "non_workable_reasons"
    __table_args__ = ({"schema": SCHEMA},)

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    reason_code = Column(String(50), nullable=False, unique=True)
    reason_description = Column(String(255), nullable=False)
