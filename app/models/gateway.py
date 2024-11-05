from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class Gateway(Base):
    __tablename__ = "gateway"
    __table_args__ = {"schema": SCHEMA}

    gateway_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True)
    serial_number = Column(String(150), nullable=False, unique=True)
    gateway_model_id = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.gateway_model.gateway_model_id", ondelete="SET NULL"),
        nullable=False,
    )
    gateway_connection_type_id = Column(
        Integer,
        ForeignKey(
            f"{SCHEMA}.gateway_connection_type.gateway_connection_type_id",
            ondelete="SET NULL",
        ),
        nullable=False,
    )
    utility_type = Column(String(20), nullable=False)
    gateway_manufacturer_code = Column(String(20), nullable=False)
    created_by = Column(String(150), nullable=False)
    slug = Column(
        UUID(as_uuid=True),
        nullable=False,
        unique=True,
        server_default=text("utility_sync.uuid_generate_v4()"),
    )
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    gateway_model = relationship("GatewayModel", back_populates="gateways")
    gateway_connection_type = relationship(
        "GatewayConnectionType", back_populates="gateways"
    )
