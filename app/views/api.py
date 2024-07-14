from typing import List
from fastapi import APIRouter, Depends, Path, Query, Request
from app.controllers.combined_controller import get_combined_data

from app.controllers.copiar_laboratorio_periodo import get_clonar_lab
from app.controllers.cursos_autodirigidos_controller import get_all_cursos_auto
from app.controllers.laboratorios_controller import add_curso, add_nodo
from app.controllers.quitar_cursos_controller import quitar_curso
from app.controllers.recursos_generales_controller import  get_all_cursos_laboratorio, get_all_cursos_laboratorio_centro_nodo, get_all_periodo, get_recursos
from app.controllers.referencia_centro import fetch_centro
from app.models.combined_model import CombinedModel
from app.models.laboratorio_curso import LaboratorioCurso, LaboratorioCursoList
from app.controllers.laboratorio_curso_controller import create_laboratorio_curso, read_laboratorio_curso
from app.sql.clonar import ADD_CURSO_LAB, ADD_CURSO_NODO, COPIAR_CURSO_AUTODIRIGIDOS, COPIAR_LAB_PERIODO, COPIAR_NODO_CENTRO, QUITAR_CURSO
from app.sql.cursos_autodirigidos_sql import GET_CURSO_AUTO_ALL
from app.sql.recursos_generales_sql import GET_ALL_LABORATORIO_CURSO_PERIODO, GET_ALL_LABORATORIO_CURSO_PERIODO_CENTRO_NODO, GET_CENTRO, GET_CURSO, GET_PERIODO, GET_PERIODO_ALL

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

@router.get("/periodosall")
def get_periodo_all(
    token: str = Query(..., title="Token a consultar")):
     return get_all_periodo(GET_PERIODO_ALL,token)


@router.get("/cursosauto")
def get_curso_auto(id: int = Query(..., title="Curso a consultar"),
    token: str = Query(..., title="Token a consultar")):
     return get_all_cursos_auto(id, GET_CURSO_AUTO_ALL,token)


@router.get("/clonarlab")
def get_copiar_lab(origen: int = Query(..., title="Periodo Origen"),
                   destino: int = Query(..., title="Periodo Destino"),
    token: str = Query(..., title="Token a consultar")):
     return get_clonar_lab(origen,destino,COPIAR_LAB_PERIODO,token)

@router.get("/clonarnodo")
def get_copiar_lab(origen: int = Query(..., title="Periodo Origen"),
                   destino: int = Query(..., title="Periodo Destino"),
    token: str = Query(..., title="Token a consultar")):
     return get_clonar_lab(origen,destino,COPIAR_NODO_CENTRO,token)

@router.get("/clonarautodirigidos")
def get_copiar_lab(origen: int = Query(..., title="Periodo Origen"),
                   destino: int = Query(..., title="Periodo Destino"),
    token: str = Query(..., title="Token a consultar")):
     return get_clonar_lab(origen,destino,COPIAR_CURSO_AUTODIRIGIDOS,token)


@router.get("/quitar")
def get_quitar(origen: str = Query(..., title="Periodo Origen"),
                   id: int = Query(..., title="Periodo Destino"),
    token: str = Query(..., title="Token a consultar")):
     return quitar_curso(origen,id,QUITAR_CURSO,token)

""" @router.post("/addlab")
def add_cursolab( 
    curso: int = Query(..., title="Curso"),
    centro: int = Query(..., title="Centro"),
    estudiantes_grupo: int = Query(..., title="Estudiantes Grupo"),
    horas_grupo: int = Query(..., title="Horas Grupo"),
    tipo_laboratorio: str = Query(None, title="Tipo de Laboratorio"),
    ubicacion: str = Query(None, title="Ubicación"),
    recurso: str = Query(None, title="Recurso"),
    periodo: int = Query(..., title="Periodo"),
    estado: int = Query(..., title="Estado"),
    token: str = Query(..., title="Token a consultar")):
    return add_curso(curso,centro,estudiantes_grupo,horas_grupo,tipo_laboratorio,ubicacion,recurso,periodo,estado,token,ADD_CURSO_LAB,token) """


@router.post("/addlab")
async def insertar_laboratorio_curso(request: Request):
    data = await request.json()
    
    # Extraer los campos del JSON
    curso = data.get("curso")
    centro = data.get("centro")
    estudiantes_grupo = data.get("estudiantes_grupo")
    horas_grupo = data.get("horas_grupo")
    tipo_laboratorio = data.get("tipo_laboratorio")
    ubicacion = data.get("ubicacion")
    recurso = data.get("recurso")
    periodo = data.get("periodo")
    estado = data.get("estado")
    token = data.get("token")
    
    # Llamar a la función add_curso
    return add_curso(curso, centro, estudiantes_grupo, horas_grupo, tipo_laboratorio, ubicacion, recurso, periodo, estado,ADD_CURSO_LAB)

@router.post("/addnodo")
async def insertar_laboratorio_nodo(request: Request):
    data = await request.json()
    
    # Extraer los campos del JSON
    curso = data.get("curso")
    centro = data.get("centro")
    centro_atender = data.get("centro_atender")
    estudiantes = data.get("estudiantes")
    horas = data.get("horas")
    periodo = data.get("periodo")
    token = data.get("token")
    
    # Llamar a la función add_curso
    return add_nodo(curso,centro,centro_atender,estudiantes,horas,periodo,ADD_CURSO_NODO)