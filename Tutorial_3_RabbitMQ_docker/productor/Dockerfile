FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /productor

COPY ./productor.py /productor.py

CMD [ "python", "/productor.py" ]
