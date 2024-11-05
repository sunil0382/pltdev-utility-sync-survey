from sqlalchemy import Column, String, Integer, TIMESTAMP, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class GatewayModel(Base):
    __tablename__ = "gateway_model"
    __table_args__ = (
        UniqueConstraint("model_name", name="gateway_model_model_name_key"),
        UniqueConstraint("slug", name="gateway_model_slug_key"),
        {"schema": SCHEMA},
    )

    gateway_model_id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(50), nullable=False, unique=True)
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
    gateways = relationship("Gateway", back_populates="gateway_model")
