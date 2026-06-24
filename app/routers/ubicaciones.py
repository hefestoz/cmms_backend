from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.models.ubicacion import Ubicacion
from app.models.usuario import Usuario, RolUsuario
from app.schemas.ubicacion import UbicacionCreate, UbicacionResponse
from app.core.dependencies import get_supervisor_or_above

router = APIRouter(prefix="/ubicaciones", tags=["Ubicaciones"])

@router.post("/", response_model=UbicacionResponse, status_code=201)
def crear_ubicacion(
    ubicacion_data: UbicacionCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_supervisor_or_above)
):
    nueva_ubicacion = Ubicacion(
        empresa_id=current_user.empresa_id,
        planta=ubicacion_data.planta,
        seccion=ubicacion_data.seccion,
        linea=ubicacion_data.linea
    )
    db.add(nueva_ubicacion)
    db.commit()
    db.refresh(nueva_ubicacion)
    return nueva_ubicacion

@router.get("/", response_model=list[UbicacionResponse])
def listar_ubicaciones(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_supervisor_or_above)
):
    return db.query(Ubicacion).filter(
        Ubicacion.empresa_id == current_user.empresa_id
    ).all()

@router.put("/{ubicacion_id}", response_model=UbicacionResponse)
def actualizar_ubicacion(
    ubicacion_id: UUID,
    ubicacion_data: UbicacionCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_supervisor_or_above)
):
    ubicacion = db.query(Ubicacion).filter(
        Ubicacion.id == ubicacion_id,
        Ubicacion.empresa_id == current_user.empresa_id
    ).first()
    if not ubicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ubicación no encontrada"
        )
    ubicacion.planta = ubicacion_data.planta
    ubicacion.seccion = ubicacion_data.seccion
    ubicacion.linea = ubicacion_data.linea
    db.commit()
    db.refresh(ubicacion)
    return ubicacion