from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class Criticidad(Base):
    __tablename__ = "criticidades"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nivel = Column(String(5), unique=True, nullable=False)
    descripcion = Column(String(300))

    equipos = relationship("Maquinaria", back_populates="criticidad")