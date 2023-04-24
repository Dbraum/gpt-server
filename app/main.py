from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .services import items, users,root

from .logging_config import logger
from dotenv import load_dotenv
import os

## 加载.env 环境变量
load_dotenv()


app = FastAPI()
## 访问变量案例
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
logger.debug(PINECONE_API_KEY)
logger.debug(PINECONE_ENVIRONMENT)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router) 
app.include_router(items.router)
app.include_router(users.router) 

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host='0.0.0.0', port=8000) 

