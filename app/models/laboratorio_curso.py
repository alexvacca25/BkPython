from typing import List, Optional
from pydantic import BaseModel


class LaboratorioCurso(BaseModel):
    id: Optional[int] = None
    curso: float
    centro: int
    estudiantes_grupo: int
    horas_grupo: float
    tipo_laboratorio: Optional[str] = None
    ubicacion: Optional[str] = None
    recurso: Optional[str] = None
    periodo: int
    estado: int


class LaboratorioCursoList(BaseModel):
    laboratorios: List[LaboratorioCurso]