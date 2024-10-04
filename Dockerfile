FROM python:alpine





ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python" ,"app.py"]

