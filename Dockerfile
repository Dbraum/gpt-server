
FROM python:3.10
WORKDIR /app
#It copies the framework and the dependencies for the FastAPI application into the working directory
COPY requirements.txt .
#It will install the framework and the dependencies in the `requirements.txt` file.
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
#It will copy the remaining files and the source code from the host `fast-api` folder to the `app` container working directory
COPY . .
#It will expose the FastAPI application on port `8000` inside the container
EXPOSE 8000
#It is the command that will start and run the FastAPI application container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]