from sqlalchemy.orm import Session
from app.models.criticidad import Criticidad

CRITICIDADES = [
    {
        "nivel": "A",
        "descripcion": "Crítico — Impacto alto en seguridad, producción o calidad. Requiere mantenimiento prioritario."
    },
    {
        "nivel": "B",
        "descripcion": "Importante — Impacto medio, afecta parcialmente la operación. Requiere mantenimiento programado."
    },
    {
        "nivel": "C",
        "descripcion": "Prescindible — Impacto bajo, no afecta producción ni seguridad. Mantenimiento correctivo aceptable."
    }
]

def seed_criticidades(db: Session):
    for item in CRITICIDADES:
        existe = db.query(Criticidad).filter(Criticidad.nivel == item["nivel"]).first()
        if not existe:
            db.add(Criticidad(nivel=item["nivel"], descripcion=item["descripcion"]))
    db.commit()