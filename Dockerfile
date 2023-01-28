FROM python:3.7-alpine

COPY bot/config.py /bot/
COPY bot/bot_rt_like.py /bot/
COPY bot/requirements /bot/
COPY .env /bot/
RUN pip3 install -r bot/requirements.txt

WORKDIR /bot
CMD ["python3", "bot_rt_like.py"]