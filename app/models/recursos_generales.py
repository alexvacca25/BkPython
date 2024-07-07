from pydantic import BaseModel


class RecursosModel(BaseModel):
    id: int
    descripcion: str
    
