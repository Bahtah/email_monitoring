FROM python:3.10.12


WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

ADD . /app/

EXPOSE 8000
RUN mkdir "static"

