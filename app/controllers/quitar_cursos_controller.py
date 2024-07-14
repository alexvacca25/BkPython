
from typing import List
from fastapi import HTTPException
import pymysql

from app.database import get_db_connection
from app.models.cursos_autodirigidos import CursoAuto

def quitar_curso(origen:str,id:int,sql: str,token:str) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            """ sql = GET_CURSO """
            
            cursor.execute(sql,(origen,id))
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