from sqlalchemy import Column, String, UUID, TIMESTAMP, BigInteger
from app.config.settings import SCHEMA
from app.database.base import Base


class Floor(Base):
    __tablename__ = "floor"
    __table_args__ = {"schema": SCHEMA}
    floor_id = Column(BigInteger, primary_key=True, autoincrement=True)
    floor_code = Column(String(20), unique=True, nullable=False)
    floor_name = Column(String(150))
    slug = Column(UUID(as_uuid=True), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now")
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default="now", onupdate="now"
    )
