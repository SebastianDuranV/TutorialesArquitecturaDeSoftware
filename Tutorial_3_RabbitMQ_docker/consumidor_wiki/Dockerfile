FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt && pip install wikipedia

ENV PYTHONUNBUFFERED=1

WORKDIR /consumidor_wiki

COPY ./consumidor_wiki.py /consumidor_wiki.py

CMD [ "python", "/consumidor_wiki.py" ]
