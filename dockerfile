FROM python:3.7-slim

MAINTAINER Kevin Janssen "xthekay@gmail.com"

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python" ,"app.py"]
