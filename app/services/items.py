from fastapi import APIRouter

from app.models import Item
from app.logging_config import logger

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")  
def get_items():
    logger.debug('route: /')
    return [Item(id=1, name="Foo"), Item(id=2, name="Bar")]