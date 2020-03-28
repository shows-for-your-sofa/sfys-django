FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /sfys-django
WORKDIR /sfys-django

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN pip install pipenv && pipenv install --system && pipenv install --dev --system

COPY . /sfys-django/