from fastapi import HTTPException

from app.models.referencia_centro import  get_centro_models2



def fetch_centro(item_id: int, token:str):
    
    response = get_centro_models2(item_id, token)
    print(response)
    #if centro is None:
    #    raise HTTPException(status_code=404, detail="No Encontrado")
    #response = {
    #    "token": token,
    #    "centro": centro or {}
    #}
    return response