from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def get_items():
    return {"hello": "world"}

@app.post("/items/")
def create_item(name: str, tag: str = None, description: str = None):
    item = {"name": name}
    if tag is not None:
        item["tag"] = tag
    if description is not None:
        item["description"] = description
    return item

@app.get("/users/")
def get_users(skip: int = 0, limit: int = 100):
    users = [f"User {_}" for _ in range(100)]
    return users[skip : skip + limit] 

