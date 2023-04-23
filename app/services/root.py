from fastapi import APIRouter,File, UploadFile
import io
import os
from PyPDF2 import PdfReader
from app.logging_config import logger
from langchain.document_loaders import PyPDFLoader
from langchain.docstore.document import Document
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
# from app.main import logger    # 引入主文件中定义的logger
import pinecone 
router = router = APIRouter( tags=["/"])

@router.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    try: 
        contents = await file.read()
        if file.content_type == "application/pdf":
            reader = PdfReader(io.BytesIO(contents))
            documents = []
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                documents.append(Document(
                        page_content=page.extract_text(),
                        metadata={"source": file.filename, "page": i},
                    ))
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            docs = text_splitter.split_documents(documents)
            # initialize pinecone
            pinecone.init(
                api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
                environment=os.getenv("PINECONE_ENVIRONMENT")  # next to api key in console
            )
            index_name = "demo"
            embeddings = OpenAIEmbeddings()
            Pinecone.from_documents(docs, embeddings, index_name=index_name)

    except Exception as e: 
        logger.exception(e)
        return {"detail": "Internal server error"}
        