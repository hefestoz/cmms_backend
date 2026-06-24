from sqlalchemy import Column, String, ForeignKey, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

from app.database import Base

class TipoDocumento(enum.Enum):
    manual = "manual"
    plano = "plano"
    certificado = "certificado"
    ficha_tecnica = "ficha_tecnica"
    otro = "otro"

class DocumentoEquipo(Base):
    __tablename__ = "documentos_equipo"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_equipo = Column(String(50), ForeignKey("maquinaria_equipos.id_equipo"), nullable=False)
    tipo_documento = Column(Enum(TipoDocumento), nullable=False)
    nombre_archivo = Column(String(200), nullable=False)
    ruta_archivo = Column(String(500), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    equipo = relationship("Maquinaria", back_populates="documentos")