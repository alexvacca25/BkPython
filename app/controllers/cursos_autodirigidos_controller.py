

from typing import List
from fastapi import HTTPException
import pymysql

from app.database import get_db_connection
from app.models.cursos_autodirigidos import CursoAuto

def get_all_cursos_auto(id:int,sql: str,token:str) :
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            """ sql = GET_CURSO """
            cursor.execute(sql,(id))
            results = cursor.fetchall()
            #results['token']=token
            if not results:
                raise HTTPException(status_code=404, detail="No related data found")
            
            return [CursoAuto(**result) for result in results]

            #return results
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()