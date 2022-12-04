FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
ENV FLASK_APP=MainScores.py

EXPOSE 8777

CMD python MainGame.py && python MainScores.py





