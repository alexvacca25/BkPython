from typing import List

from app.database import get_db_connection
from app.models.laboratorio_curso import LaboratorioCurso
from fastapi import HTTPException
import pymysql

def create_laboratorio_curso(laboratorio_curso: LaboratorioCurso) -> LaboratorioCurso:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO laboratorios_cursos_centros (curso, centro, estudiantes_grupo, horas_grupo, tipo_laboratorio, ubicacion, recurso, periodo, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (laboratorio_curso.curso, laboratorio_curso.centro, laboratorio_curso.estudiantes_grupo, laboratorio_curso.horas_grupo, laboratorio_curso.tipo_laboratorio, laboratorio_curso.ubicacion, laboratorio_curso.recurso, laboratorio_curso.periodo, laboratorio_curso.estado))
            connection.commit()
            laboratorio_curso.id = cursor.lastrowid
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()
    return laboratorio_curso

def read_laboratorio_curso(laboratorio_curso_periodo: int) -> List[LaboratorioCurso]:
    connection = get_db_connection()
    
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            print('Entre aqui?')
            sql = "SELECT * FROM laboratorios_cursos_centro WHERE periodo = %s"
            cursor.execute(sql, (laboratorio_curso_periodo,))
            print('Consulta')
            results = cursor.fetchall()
            if not results:
                raise HTTPException(status_code=404, detail="No LaboratorioCursos found")
            return [LaboratorioCurso(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

def read_laboratorio_curso_list(laboratorio_curso_periodo: int) -> List[LaboratorioCurso]:
    connection = get_db_connection()
    
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            print('Entre aqui?')
            sql = "SELECT * FROM laboratorios_cursos_centro WHERE periodo = %s"
            cursor.execute(sql, (laboratorio_curso_periodo,))
            print('Consulta')
            results = cursor.fetchall()
            if not results:
                raise HTTPException(status_code=404, detail="No LaboratorioCursos found")
            return [LaboratorioCurso(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()