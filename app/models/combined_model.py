from pydantic import BaseModel
from typing import Optional

class CombinedModel(BaseModel):
    id:Optional[int]
    id_curso: Optional[float]
    curso_descripcion: Optional[str]
    centro: Optional[int]
    nombrecead: Optional[str]
    estudiantes_grupo: Optional[int]
    horas_grupo: Optional[float]
    tipo_laboratorio: Optional[str]
    ubicacion: Optional[str]
    recurso: Optional[str]
    token:Optional[str]
