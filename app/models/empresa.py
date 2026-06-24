from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(200), nullable=False)
    nit = Column(String(20), unique=True, nullable=False)
    plan_suscripcion = Column(String(50), default="basico")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    usuarios = relationship("Usuario", back_populates="empresa")
    equipos = relationship("Maquinaria", back_populates="empresa")
    ubicaciones = relationship("Ubicacion", back_populates="empresa")