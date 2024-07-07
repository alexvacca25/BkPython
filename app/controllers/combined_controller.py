from app.database import get_db_connection
from app.models.combined_model import CombinedModel
from fastapi import HTTPException
import pymysql
from typing import List

def get_combined_data(periodo: int, token: str) -> List[CombinedModel]:
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
            SELECT 
   
                lc.curso AS id_curso,
                ac.curso_descripcion ,
                lc.centro ,
                rc.nombrecead ,
                lc.estudiantes_grupo, 
                lc.horas_grupo, 
                lc.tipo_laboratorio, 
                lc.ubicacion, 
                lc.recurso   
                    

                FROM 
                soca2023.laboratorios_cursos_centro lc,
                soca2023.aad_cursos ac,
                soca2023.referencia_centro rc


                WHERE 
                lc.curso = ac.curso_equivalente and
                lc.centro = rc.codigocead and 
                lc.periodo = %s;

            """
            cursor.execute(sql, (periodo,))
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
