from typing import Optional
from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(String, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    correo = Column(String(100))