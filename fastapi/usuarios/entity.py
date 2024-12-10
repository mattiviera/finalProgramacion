from typing import Optional
from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre: str 
    edad: Optional[int]  
    correo: str  