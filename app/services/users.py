from fastapi import APIRouter

from app.models import User

router = APIRouter(prefix="/users", tags=["users"])

users_db = [User(id=1, name="John",email="wukunpeng@deepexi.com"), User(id=2, name="Jane",email="yanglei@deepexi.com")]

@router.get("/")  
def get_users():
    return users_db