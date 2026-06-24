from sqlalchemy import Column, String, Date, Float, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum

from app.database import Base

class TipoOrden(enum.Enum):
    preventivo = "preventivo"
    correctivo = "correctivo"

class EstadoOrden(enum.Enum):
    abierta = "abierta"
    pendiente_repuestos = "pendiente_repuestos"
    cerrada = "cerrada"

class OrdenTrabajo(Base):
    __tablename__ = "ordenes_trabajo"

    id_orden = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_equipo = Column(String(50), ForeignKey("maquinaria_equipos.id_equipo"), nullable=False)
    id_plan = Column(UUID(as_uuid=True), ForeignKey("planes_mantenimiento.id_plan"), nullable=True)
    id_tecnico = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False)
    tipo_orden = Column(Enum(TipoOrden), nullable=False)
    fecha_programada = Column(Date)
    fecha_ejecucion = Column(Date)
    horas_paro = Column(Float)
    descripcion_trabajo = Column(Text)
    costo_materiales = Column(Float)
    estado_orden = Column(Enum(EstadoOrden), default=EstadoOrden.abierta, nullable=False)

    equipo = relationship("Maquinaria", back_populates="ordenes")
    plan = relationship("PlanMantenimiento", back_populates="ordenes")
    tecnico = relationship("Usuario", back_populates="ordenes")