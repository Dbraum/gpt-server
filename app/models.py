from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str

class User(BaseModel):
    id: int
    name: str 
    email: str