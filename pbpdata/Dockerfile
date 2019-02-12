
# Dockerfile

FROM python:3.7-slim as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app

EXPOSE 8000
CMD ["gunicorn", "-w 4", "-b :8000", "pbpdata.wsgi"]
