
from typing import List
from fastapi import HTTPException
import pymysql

from app.database import get_db_connection


def add_curso(curso:int,centro:int,estudiantes_grupo:int,horas_grupo:int,tipo_laboratorio:str,ubicacion:str,recurso:str,periodo:int,estado:int, sql) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            """ sql = GET_CURSO """
            
            cursor.execute(sql,(curso,centro,estudiantes_grupo,horas_grupo,tipo_laboratorio,ubicacion,recurso,periodo,estado))
            connection.commit()
            results = cursor.fetchone()
            
            #results['token']=token
            if not results:
                raise HTTPException(status_code=404, detail="No related data found")
            
            return results

            #return results
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()


def add_nodo(curso,centro,centro_atender,estudiantes,horas,periodo, sql) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            """ sql = GET_CURSO """
            
            cursor.execute(sql,(curso,centro,centro_atender,estudiantes,horas,periodo))
            connection.commit()
            results = cursor.fetchone()
            
            #results['token']=token
            if not results:
                raise HTTPException(status_code=404, detail="No related data found")
            
            return results

            #return results
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()