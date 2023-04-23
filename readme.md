# FastAPI for gpt start


## 环境准备
You'll must have installed:
- [Python 3.6+](https://www.python.org/downloads/)
- [Virtual Environments with Python3.6+](https://docs.python.org/3/tutorial/venv.html)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker-compose](https://docs.docker.com/compose/install/)
___
## 开发环境搭建

```bash
git clone https://gitlab.deepexi.com/sig/gpt-server.git
cd gpt-server
# Create virtual environment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
# Starting application, run:
uvicorn app.main:app --reload
```


## Acessing on local
The application will get started in http://127.0.0.1:8000  

Swagger Documentation: http://127.0.0.1:8000/docs

Redoc Documentation: http://127.0.0.1:8000/redoc

## TODO

- [] 环境变量配置化
- [] 增加安全认证
- [] 业务代码分层
- [] 代码结构文档描述

## Development

For update dependencies on `requirements.txt`, run:  


```bash
pip freeze > requirements.txt
```


### Source Documentation
- [FastAPI](https://fastapi.tiangolo.com/)

- [Bigger Application](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

- [SQL](https://fastapi.tiangolo.com/tutorial/sql-databases/)

- [Testing](https://fastapi.tiangolo.com/tutorial/testing/)  

- [Pydantic](https://pydantic-docs.helpmanual.io/)  

- [SQL Relational Database SQLAlchemy by FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=databa#sql-relational-databases)

- [SQLAlchemy 1.4](https://docs.sqlalchemy.org/en/14/tutorial/engine.html)  

- [FastAPI "Real world example app"](https://github.com/nsidnev/fastapi-realworld-example-app)  

