from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum

from app.database import Base

class TipoMantenimiento(enum.Enum):
    preventivo = "preventivo"
    predictivo = "predictivo"
    lubricacion = "lubricacion"
    calibracion = "calibracion"

class PlanMantenimiento(Base):
    __tablename__ = "planes_mantenimiento"

    id_plan = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_equipo = Column(String(50), ForeignKey("maquinaria_equipos.id_equipo"), nullable=False)
    nombre_tarea = Column(String(200), nullable=False)
    frecuencia_dias = Column(Integer)
    frecuencia_horas = Column(Integer)
    tipo_mantenimiento = Column(Enum(TipoMantenimiento), nullable=False)
    id_procedimiento = Column(String(50))

    equipo = relationship("Maquinaria", back_populates="planes")
    ordenes = relationship("OrdenTrabajo", back_populates="plan")