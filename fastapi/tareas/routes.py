from fastapi import APIRouter, HTTPException
from tareas.dto import TareaDTO, TareaCreateDTO, TareaUpdateDTO
from tareas.service import *

tarea_router = APIRouter()

@tarea_router.get('/', response_model=list[TareaDTO], status_code=200)
async def get_all_tareas():
    tareas = await get_tareas()
    if not tareas:
        raise HTTPException(status_code=404, detail="No se encontraron tareas")
    return tareas

@tarea_router.get('/{id}', response_model=TareaDTO, status_code=200)
async def get_tarea(id: str):
    tarea = await get_tarea_by_id(id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@tarea_router.post('/', response_model=TareaDTO, status_code=201)
async def create_tarea(tarea: TareaCreateDTO):
    nueva_tarea = await create_tarea(tarea)
    if not nueva_tarea:
        raise HTTPException(status_code=400, detail="No se pudo crear la tarea")
    return nueva_tarea

@tarea_router.put('/{id}', response_model=TareaDTO, status_code=200)
async def update_tarea(id: str, tarea_update: TareaUpdateDTO):
    tarea_actualizada = await update_tarea(id, tarea_update)
    if not tarea_actualizada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no actualizada")
    return tarea_actualizada

@tarea_router.delete('/{id}', response_model=TareaDTO, status_code=200)
async def delete_tarea(id: str):
    tarea_eliminada = await delete_tarea(id)
    if not tarea_eliminada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no eliminada")
    return tarea_eliminada
