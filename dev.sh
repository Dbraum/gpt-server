virtualenv env
source ${PWD}/env/bin/activate 
pip install --upgrade pip       
pip install -r requirements.txt --force-reinstall
deactivate
source ${PWD}/env/bin/activate
uvicorn app.main:app --reload