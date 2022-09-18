FROM python:3.10-alpine

COPY . /app
WORKDIR /app

RUN pip install Flask
RUN pip install requests
RUN pip install selenium

CMD python3 MainGame.py




