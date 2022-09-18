FROM python:3.10-alpine

COPY . /app
WORKDIR /app

RUN pip install Flask
RUN pip install requests

CMD python3 MainGame.py
CMD python3 MainSores.py



