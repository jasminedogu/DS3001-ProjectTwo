FROM python:3.7-alpine

COPY bots/quotesmaker.py /bots/
COPY bots/tweetReply.py /bots/
COPY requirements.txt /tmp
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
    
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "tweetReply.py"]