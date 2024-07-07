from typing import List
from fastapi import APIRouter, Depends, Path, Query
from app.controllers.combined_controller import get_combined_data

from app.controllers.recursos_generales_controller import  get_all_cursos_laboratorio, get_all_cursos_laboratorio_centro_nodo, get_recursos
from app.controllers.referencia_centro import fetch_centro
from app.models.combined_model import CombinedModel
from app.models.laboratorio_curso import LaboratorioCurso, LaboratorioCursoList
from app.controllers.laboratorio_curso_controller import create_laboratorio_curso, read_laboratorio_curso
from app.sql.recursos_generales_sql import GET_ALL_LABORATORIO_CURSO_PERIODO, GET_ALL_LABORATORIO_CURSO_PERIODO_CENTRO_NODO, GET_CENTRO, GET_CURSO, GET_PERIODO

from auth.dependencies import validar_token_en_api_externa


router = APIRouter()

@router.post("/laboratorios_cursos/", response_model=LaboratorioCurso)
def create_laboratorio_curso_view(laboratorio_curso: LaboratorioCurso):
    return create_laboratorio_curso(laboratorio_curso)

@router.get("/laboratorios_cursos/{laboratorio_curso_periodo}", response_model=LaboratorioCursoList)
def read_laboratorio_curso_view(laboratorio_curso_periodo: int):
    laboratorios = read_laboratorio_curso(laboratorio_curso_periodo)
    return LaboratorioCursoList(laboratorios=laboratorios)



@router.get("/combined_data", response_model=List[CombinedModel])
def get_combined_data_view(periodo: int = Query(..., title="Periodo a consultar"),
    token: str = Query(..., title="Periodo a consultar")):
    #print(token)
    return get_combined_data(periodo,token)

#@router.get("/combined_data", response_model=List[CombinedModel])
#def get_combined_data_view(periodo: int = Query(..., title="Periodo a consultar"),
#    token: str = Depends(validar_token_en_api_externa)):
#    #print(token)
#    return get_combined_data(periodo,token)



#@router.get("/centro")
#def get_centro_id(codigocead: int = Query(..., title="Centro a consultar"),
#    token: str = Depends(validar_token_en_api_externa)):
#    return fetch_centro(codigocead,token)

""" @router.get("/centro")
def get_centro_id(codigocead: int = Query(..., title="Centro a consultar"),
    token: str = Query(..., title="Token a consultar")):
    return fetch_centro(codigocead,token)
 """


@router.get("/curso")
def get_curso_id(id: int = Query(..., title="Curso a consultar"),
    token: str = Query(..., title="Token a consultar")):
    return get_recursos(id, GET_CURSO)

@router.get("/centro")
def get_centro_id(id: int = Query(..., title="Curso a consultar"),
    token: str = Query(..., title="Token a consultar")):
     return get_recursos(id, GET_CENTRO)

@router.get("/periodo")
def get_periodo_id(id: int = Query(..., title="Curso a consultar"),
    token: str = Query(..., title="Token a consultar")):
     return get_recursos(id, GET_PERIODO)

@router.get("/laboratorios")
def get_laboratorios(id: int = Query(..., title="Curso a consultar"),
    token: str = Query(..., title="Token a consultar")):
     return get_all_cursos_laboratorio(id, GET_ALL_LABORATORIO_CURSO_PERIODO,token)

@router.get("/labnodos")
def get_lab_nodos(id: int = Query(..., title="Curso a consultar"),
    token: str = Query(..., title="Token a consultar")):
     return get_all_cursos_laboratorio_centro_nodo(id, GET_ALL_LABORATORIO_CURSO_PERIODO_CENTRO_NODO,token)