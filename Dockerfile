FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /sfys-django
WORKDIR /code
COPY requirements.txt /sfys-django/
RUN pip install -r requirements.txt
COPY . /sfys-django/