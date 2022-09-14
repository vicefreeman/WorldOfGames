FROM python:3.10-alpine

COPY . /app

RUN pip install Flask
RUN pip install requests

CMD python3 /app/MainGame.py


