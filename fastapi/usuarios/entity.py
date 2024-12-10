from typing import Optional
from default.defaultmodel import Base
class Usuario(Base):
    __tablename__ = 'usuarios'

    id: int  
    nombre: str 
    edad: Optional[int]  
    correo: str  