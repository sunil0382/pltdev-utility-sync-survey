from sqlalchemy import Column, String, UUID, TIMESTAMP, BigInteger
from app.config.settings import SCHEMA
from app.database.base import Base


class Room(Base):
    __tablename__ = "room"
    __table_args__ = {"schema": SCHEMA}

    room_id = Column(BigInteger, primary_key=True, autoincrement=True)
    room_code = Column(String(10), unique=True, nullable=False)
    room_name = Column(String(50))
    slug = Column(UUID(as_uuid=True), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default="now")
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default="now", onupdate="now"
    )
