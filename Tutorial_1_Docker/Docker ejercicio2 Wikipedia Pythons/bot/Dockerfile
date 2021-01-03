FROM python:3.6.3

#ENV MONGO_HOST localhost
#ENV MONGO_PORT 27017
#ENV SLACK_TOKEN="xoxb-77335436279-1431847376817-6Z9s1ODePKMgqLt7eoAh6Gr9"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /bot

COPY ./app.py /app.py

CMD [ "python", "/app.py" ]
