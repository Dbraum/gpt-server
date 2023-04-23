from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/")
def read_root():
    return {"Hello": "World"}

@api_router.get("/items/") 
def read_items():
    return ["Item1", "Item2"] 

@api_router.get("/users/{user_id}")  
def read_user(user_id: int): 
    return {"user_id": user_id}