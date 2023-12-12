FROM python:bookworm

WORKDIR /bot
COPY ./requirements.txt /bot/
RUN pip install -r requirements.txt

COPY . /bot/

CMD ["python", "app/main.py"]
