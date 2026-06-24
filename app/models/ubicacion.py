from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    empresa_id = Column(UUID(as_uuid=True), ForeignKey("empresas.id"), nullable=False)
    planta = Column(String(100), nullable=False)
    seccion = Column(String(100))
    linea = Column(String(100))

    empresa = relationship("Empresa", back_populates="ubicaciones")
    equipos = relationship("Maquinaria", back_populates="ubicacion")