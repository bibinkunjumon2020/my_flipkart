# pull the official base image
FROM python:3.9.5-slim
# with in image working directory
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# copy project
COPY . .
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt # install all packages
#RUN pip install psycopg2-binary # gave separately because not installed by above call.