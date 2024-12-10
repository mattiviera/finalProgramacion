from pydantic import BaseModel
from typing import Optional

class UsuarioDTO(BaseModel):
    id: str
    nombre: str
    edad: int
    correo: str

class UsuarioCreateDTO(BaseModel):
    nombre: str
    edad: int
    correo: str

class UsuarioUpdateDTO(BaseModel):
    nombre: Optional[str]
    edad: Optional[int]
    correo: Optional[str]

class DeleteUsuarioDTO(BaseModel):
    id: str