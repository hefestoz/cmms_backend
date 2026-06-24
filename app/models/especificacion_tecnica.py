from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class EspecificacionTecnica(Base):
    __tablename__ = "especificaciones_tecnicas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_equipo = Column(String(50), ForeignKey("maquinaria_equipos.id_equipo"), nullable=False)
    parametro_clave = Column(String(100), nullable=False)
    valor_parametro = Column(String(200), nullable=False)
    unidad = Column(String(30))

    equipo = relationship("Maquinaria", back_populates="especificaciones_tecnicas")