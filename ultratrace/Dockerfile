# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
COPY . .
COPY __main__.py app.py
COPY requirements.txt requirements.txt
RUN apt-get update -y
RUN apt-get install -y python3 portaudio19-dev libportaudio2 ffmpeg
RUN pip3 install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]