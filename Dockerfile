FROM python:3.10-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
ENV FLASK_APP=Score.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 3000

CMD python MainGame.py
CMD ["flask", "run"]




