
# Dockerfile

FROM python:3.7-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install

# Need this stuff to build postgres driver on Alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /requirements.txt
RUN pip install -U pip
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
RUN apk add postgresql-client
# so emacs docker-tramp will work...
RUN apk add bash
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app

EXPOSE 8000
CMD ["gunicorn", "-w 4", "-b :8000", "pbpdata.wsgi"]
