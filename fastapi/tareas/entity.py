from typing import Optional
from datetime import date
from sqlalchemy.orm import relationship
from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Tarea(Base):
    __tablename__ = 'tareas'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    tarea = Column(String(50))  
    fecha = Column(Date)
    id_estado = Column(Integer, ForeignKey('estados_tareas.id'))

usuario = relationship("Usuario", back_populates="tareas")

estado = relationship("Estado", back_populates="tareas")