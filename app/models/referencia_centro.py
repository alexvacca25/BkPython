

import json
from fastapi import HTTPException
from app.database import get_db_connection
from app.sql.recursos_generales_sql import GET_CENTRO



def get_centro_models(codigocead):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    print('aqui')
    cursor.execute(GET_CENTRO, (codigocead,))
    item = cursor.fetchone()
    print(item)
    cursor.close()
    connection.close()
    return item

def get_centro_models2(codigocead,token):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = GET_CENTRO
            cursor.execute(sql, (codigocead))
            connection.commit()
            results = cursor.fetchone()
            print(results)
            #print(results)
            #if not results:
            #    raise HTTPException(status_code=404, detail="Centro No Encontrado")
            #data = [dict(zip(['codigocead', 'nombrecead'], row)) for row in results]
            #json_data =json.loads(json.dumps(data))
            json_data = dict(zip(['codigocead', 'nombrecead'], results))
            json_data['token'] = token
            return json_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()
        cursor.close()