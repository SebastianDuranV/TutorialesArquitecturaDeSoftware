FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt && pip install --upgrade google-api-python-client

ENV PYTHONUNBUFFERED=1

WORKDIR /consumidor_youtube

COPY ./consumidor_youtube.py /consumidor_youtube.py

CMD [ "python", "/consumidor_youtube.py" ]
