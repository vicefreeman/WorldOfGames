FROM ubuntu

COPY . /app

RUN pip install Flask
RUN pip install Python3

CMD python3 /app/MainGame.py


