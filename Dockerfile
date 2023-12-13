FROM python:bookworm

RUN apt update; apt -y upgrade; apt -y install ffmpeg

WORKDIR /bot
COPY ./requirements.txt /bot/
RUN pip install -r requirements.txt

COPY . /bot/

RUN mkdir waves

CMD ["python", "app/main.py"]
