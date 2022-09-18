FROM tiangolo/uwsgi-nginx-flask

COPY . /app

RUN pip install Flask
RUN pip install requests

CMD python3 /app/MainGame.py



