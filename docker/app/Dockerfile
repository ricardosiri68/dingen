FROM python:3.7-slim

RUN apt update && apt install libpq-dev posgresql-client
WORKDIR /site
COPY ./ /site
RUN pip install -U -r /site/requirements.txt