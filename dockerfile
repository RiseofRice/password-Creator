FROM python:3.7
MAINTAINER Kevin Janssen "xthekay@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
