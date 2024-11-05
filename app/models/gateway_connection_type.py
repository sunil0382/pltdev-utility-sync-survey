from sqlalchemy import Column, String, Integer, TIMESTAMP, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class GatewayConnectionType(Base):
    __tablename__ = "gateway_connection_type"
    __table_args__ = (
        UniqueConstraint(
            "connection_code", name="gateway_connection_type_connection_code_key"
        ),
        UniqueConstraint("slug", name="gateway_connection_type_slug_key"),
        {"schema": SCHEMA},
    )

    gateway_connection_type_id = Column(Integer, primary_key=True, autoincrement=True)
    connection_code = Column(String(50), nullable=False, unique=True)
    description = Column(String(100))
    slug = Column(
        UUID(as_uuid=True),
        nullable=False,
        unique=True,
        server_default=text("utility_sync.uuid_generate_v4()"),
    )
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )
    gateways = relationship("Gateway", back_populates="gateway_connection_type")
