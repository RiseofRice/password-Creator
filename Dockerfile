FROM python:3.12-slim

MAINTAINER Kevin Janssen "xthekay@gmail.com"

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python" ,"app.py"]

