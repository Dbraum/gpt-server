from fastapi import APIRouter,File, UploadFile,BackgroundTasks
from fastapi.responses import JSONResponse
import io
import os
import pinecone 

from PyPDF2 import PdfReader
from app.logging_config import logger
from langchain.docstore.document import Document
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings


router = router = APIRouter( tags=["/"])


@router.post("/uploadfile")
async def create_upload_file(background_tasks: BackgroundTasks,file: UploadFile = File(...)):
    # todo: 目前通过异步进程进行pdf解析，生产开启多线程模式增加下并发，后续需要将这些解析任务
    # 剥离到别的服务
    if file.content_type != "application/pdf":
            return JSONResponse(status_code=400, content={"error": "Only .pdf files are allowed!"})
    logger.debug("上传文件名称："+ file.filename)
    background_tasks.add_task(read_pdf, file)
    return {"message": "PDF processing in the background!"}
   

async def read_pdf(file):
    try: 
        contents = await file.read()
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
        index_name = os.getenv("PINECONE_INDEX_NAME")
        embeddings = OpenAIEmbeddings()
        docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
        query = "benefits of using snowflake"
        docs = docsearch.similarity_search(query)
        logger.info(docs[0].page_content)
            

    except Exception as e: 
        logger.exception(e)