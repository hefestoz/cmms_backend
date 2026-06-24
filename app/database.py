from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# motor de conexiones a la base de datos
engine = create_engine(DATABASE_URL)

# usada oara crear sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# clase base de datos
Base = declarative_base()

# sesion unica para la aplicacion — se usa como dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()