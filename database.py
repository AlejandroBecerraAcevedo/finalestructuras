from sqlalchemy import create_engine   
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


URL_DATABASE = 'postgresql://administrador:admin@localhost:5432/bd_estructura'  


engine = create_engine(URL_DATABASE)   
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bin=engine)     
Base = declarative_base()  