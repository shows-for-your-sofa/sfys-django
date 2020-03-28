FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /sfys-django
WORKDIR /sfys-django
COPY requirements.txt /sfys-django/
RUN pip install -r requirements.txt
COPY . /sfys-django/