FROM python:3.10-alpine

COPY . /app

RUN pip install Flask

CMD flask --app ./MainGame.py run


