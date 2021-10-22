FROM python:3-alpine

ENV CRON_SIGNIN='0 7 * * *'

WORKDIR /app

ADD requirements.txt  ./
COPY docker.py ./
COPY helper ./helper

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir crontab 

CMD [ "python3", "/app/docker.py" ]