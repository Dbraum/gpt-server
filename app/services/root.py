from fastapi import APIRouter,File, UploadFile
import io
from PyPDF2 import PdfReader
from app.logging_config import logger
# from app.main import logger    # 引入主文件中定义的logger

router = router = APIRouter( tags=["/"])

@router.post("/uploadfile")
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