from pydantic import BaseModel
from typing import List

class CentroAtendido(BaseModel):
    idCentroAtender: int
    centro_atender: int
    nombre_centro_atendido: str

class CursoConCentros(BaseModel):
    id:int
    curso: int
    descripcion: str
    centro: int
    nombre_centro_principal:str
    estudiantes:int
    horas:int
    periodo:int
    atiende: List[CentroAtendido]
    zona:str
    escuela:str
    tipo:str