FROM python:3.10-alpine

COPY . /app

RUN pip install Flask

CMD python3 /app/MainGame.py


