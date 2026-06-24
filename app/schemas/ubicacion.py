from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class UbicacionCreate(BaseModel):
    planta: str
    seccion: Optional[str] = None
    linea: Optional[str] = None

class UbicacionResponse(BaseModel):
    id: UUID
    empresa_id: UUID
    planta: str
    seccion: Optional[str] = None
    linea: Optional[str] = None

    model_config = {"from_attributes": True}