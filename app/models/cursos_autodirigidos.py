from pydantic import BaseModel
from typing import Optional

class CursoAuto(BaseModel):
    id: int
    periodo: int
    curso: int
    consecutivo: int
    mat_descripcion: str
    escuela_descripcion: str