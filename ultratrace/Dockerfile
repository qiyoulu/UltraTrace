# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y apt-utils python3 ffmpeg portaudio19-dev libportaudio2 ffmpeg wxpython-tools python3-flask

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY __main__.py app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]