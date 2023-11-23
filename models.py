from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from database import Base


 

class Unidad_Academica(Base):
    __tablename__ = 'unidad_academica'
    id_unidad_academica = Column(Integer, primary_key=True, index=True)
    nombre_unidad_academica = Column(String)
    municipio = Column(String)  
    
    
class Estudiante(Base):
    __tablename__ = 'estudiante'
    id_estudiante = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String)
    numero_identidad = Column(String)
    genero = Column(String)
    estrato = Column(Integer)
    fecha_nacimiento = Column(DateTime)
    id_carrera = Column(Integer, ForeignKey('carrera.id_carrera'))
   
    
    
class Carrera(Base):
    __tablename__ = 'carrera'
    id_carrera = Column(Integer, primary_key=True, index=True)
    nombre_carrera = Column(String)
    id_unidad_academica = Column(Integer, ForeignKey('unidad_academica.id_unidad_academica'))
    
    
    

    
    
