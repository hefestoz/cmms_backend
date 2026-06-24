from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum

class RolUsuario(str, Enum):
    superadmin = "superadmin"
    admin = "admin"
    supervisor = "supervisor"
    tecnico = "tecnico"

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    rol: RolUsuario = RolUsuario.tecnico

class UsuarioResponse(BaseModel):
    id: UUID
    nombre: str
    email: EmailStr
    rol: RolUsuario
    activo: bool

    model_config = {"from_attributes": True}