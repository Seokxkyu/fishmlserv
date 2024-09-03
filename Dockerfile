# FROM python:3.11
FROM datamario24/python311scikitlearn-fastapi:1.0.0

WORKDIR /code

# COPY . /code/
COPY src/fishmlserv/main.py /code/
# COPY requirements.txt /code/

# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install git+https://github.com/Seokxkyu/fishmlserv.git@0.8/DHub

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
