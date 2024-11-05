from sqlalchemy import Integer, String, Text
from sqlalchemy.testing.schema import Column
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterMigrationLog(Base):
    __tablename__ = "meter_migration_logs"
    __table_args__ = {"schema": SCHEMA}  # Add schema

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    meter_serial = Column(String(100), nullable=True)
    error_message = Column(Text, nullable=True)
