FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 3000

CMD python MainGame.py





