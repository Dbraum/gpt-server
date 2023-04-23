from fastapi import APIRouter,File, UploadFile
import io
from PyPDF2 import PdfReader
from app.logging_config import logger
# from app.main import logger    # 引入主文件中定义的logger

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

@api_router.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    
    if file.content_type == "application/pdf":
        reader = PdfReader(io.BytesIO(contents))
        pages = len(reader.pages)
        text = reader.pages[pages-1].extract_text()
        logger.debug(text)
        # do something with pdf info
    else:
        return {"error": "Unsupported file type"}
        
    return {"message": text} 