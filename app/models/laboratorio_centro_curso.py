from typing import List, Optional
from pydantic import BaseModel


class LaboratorioCentroCurso(BaseModel):
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
    token: Optional[str]


class LaboratorioCursoList(BaseModel):
    laboratorios: List[LaboratorioCentroCurso]