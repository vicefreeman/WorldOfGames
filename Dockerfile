FROM python:3.10-alpine

COPY . /app
WORKDIR /app

RUN pip install Flask
RUN pip install requests
RUN pip install selenium

EXPOSE 3000

CMD python MainGame.py
CMD python Score.py




