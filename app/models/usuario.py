from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

from app.database import Base

class RolUsuario(enum.Enum):
    admin = "admin"
    tecnico = "tecnico"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    empresa_id = Column(UUID(as_uuid=True), ForeignKey("empresas.id"), nullable=False)
    nombre = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    rol = Column(Enum(RolUsuario), default=RolUsuario.tecnico, nullable=False)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    empresa = relationship("Empresa", back_populates="usuarios")
    ordenes = relationship("OrdenTrabajo", back_populates="tecnico")