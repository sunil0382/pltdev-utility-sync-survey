from sqlalchemy import Integer, String, Text
from sqlalchemy.testing.schema import Column
from app.config.settings import SCHEMA
from app.database.base import Base


class MigrationLog(Base):
    __tablename__ = "migration_logs"
    __table_args__ = {"schema": SCHEMA}  # Add schema

    migration_log_id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True
    )
    utility_number = Column(String(100), nullable=True)
    error_message = Column(Text, nullable=True)
