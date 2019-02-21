FROM ubuntu:latest 

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential


ADD . /app
ENV HOME=/app
WORKDIR /app


RUN pip install flask
RUN pip install pymysql

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]
