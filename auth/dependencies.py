from fastapi import Depends, HTTPException, Query
from fastapi.security import OAuth2PasswordBearer
import requests 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token_with_external_server(token: str):
    validation_url = "https://thumano.unad.edu.co/apptesteo-sighum-backend/api/auth/renew"
    response = requests.get(validation_url, headers={"Authorization": f"Bearer {token}"})
    print(response)
    if response.status_code != 200:
        raise HTTPException(
            status_code=401,
            detail="Token validation failed",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return response.json()

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token_with_external_server(token)
        print(payload)
        return payload
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Token validation error",
            headers={"WWW-Authenticate": "Bearer"},
        )

def validar_token_en_api_externa(token: str = Query(title="Token de autenticación")):
    url_validacion_token = "https://thumano.unad.edu.co/apptesteo-sighum-backend/api/auth/renew"
    
    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        #print(token)
        # Realizar la solicitud GET a la URL externa para validar el token
        response = requests.get(url_validacion_token, headers=headers)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            #print(response.json().get('token'))
            return  response.json().get('token')  # Devolver el token validado
        else:
            raise HTTPException(status_code=401, detail="Token inválido")
    
    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Error de conexión con la URL externa")