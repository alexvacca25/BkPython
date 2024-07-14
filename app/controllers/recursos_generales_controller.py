
from typing import List
from fastapi import HTTPException
import pymysql

from app.database import get_db_connection
from app.models.laboratorio_curso_centro_nodo import CentroAtendido, CursoConCentros
from app.models.recursos_generales import RecursosModel



def get_recursos(id: int, sql: str) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            """ sql = GET_CURSO """
            cursor.execute(sql, (id,))
            results = cursor.fetchone()
            #results['token']=token
            if not results:
                raise HTTPException(status_code=404, detail="No related data found")
            
            return RecursosModel(**results) 

            #return results
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

def get_all_periodo(sql: str,token:str) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            """ sql = GET_CURSO """
            cursor.execute(sql,)
            results = cursor.fetchall()
            #results['token']=token
            if not results:
                raise HTTPException(status_code=404, detail="No related data found")
            
            return [RecursosModel(**result) for result in results]

            #return results
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

def get_all_cursos_laboratorio(id: int, sql: str, token:str) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            
            cursor.execute(sql, (id,))
            results = cursor.fetchall()
            #results['token']=token
            if not results:
                raise HTTPException(status_code=404, detail="No related data found")
            
            for result in results:
                result['token'] = token

            return results
            #return [CombinedModel(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()


def get_all_cursos_laboratorio_centro_nodo(id: int, sql: str, token:str) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            
            cursor.execute(sql, (id,))
            results = cursor.fetchall()
            #results['token']=token
            if not results:
                raise HTTPException(status_code=404, detail="No related data found")
            
            datos_crudos = results
            cursos = {}
            for dato in datos_crudos:
               
                key = (dato['curso'], dato['centro'])
                if key not in cursos:
                    cursos[key] = CursoConCentros(
                        id=dato['id'],
                        curso=dato['curso'],
                        descripcion=dato['descripcion'],
                        centro=dato['centro'],
                        nombre_centro_principal=dato['nombre_centro_principal'],
                        estudiantes=dato['estudiantes'],
                        horas=dato['horas'],
                        periodo=dato['periodo'],
                        zona=dato['zona'],
                        escuela=dato['escuela'],
                        tipo=dato['tipo'],
                       
                        atiende=[]
                    )
                cursos[key].atiende.append(CentroAtendido(
                    idCentroAtender=dato['id'],
                    centro_atender=dato['centro_atender'],
                    nombre_centro_atendido=dato['nombre_centro_atendido']
                ))

            return list(cursos.values())
            
            #for result in results:
            #    result['token'] = token

            #return results
            #return [CombinedModel(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

