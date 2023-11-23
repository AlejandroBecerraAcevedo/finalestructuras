from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel  
from typing import List,Annotated
from datetime import datetime as DateTime
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Estudiante(BaseModel):
    id_estudiante: int
    nombre_completo: str
    numero_identidad: str
    genero: str
    estrato: int
    fecha_nacimiento: DateTime
    id_carrera: int
    
class Carrera(BaseModel):
    id_carrera: int
    nombre_carrera: str
    id_unidad_academica: int
    
class Unidad_Academica(BaseModel):
    id_unidad_academica: int
    nombre_unidad_academica: str
    municipio: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  
        
        
        
db_dependency = Annotated[Session,Depends(get_db)] 

@app.post("/unidad_academica/")
async def create_unidad_academica(unidad_academica: Unidad_Academica,db: db_dependency):
    db_unidad_academica = models.Unidad_Academica(id_unidad_academica=unidad_academica.id_unidad_academica,nombre_unidad_academica=unidad_academica.nombre_unidad_academica,municipio=unidad_academica.municipio)
    db.add(db_unidad_academica)
    db.commit()
    db.refresh(db_unidad_academica)
    
    