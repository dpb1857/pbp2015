
GATEWAY = localhost:5432
DATABASE_URL = postgres://${GATEWAY}/pbp2015

help:
	@echo "Targets:"
	@echo "  make build"

runserver:
	PGUSER=pbp2015 DATABASE_URL=${DATABASE_URL} ./manage.py runserver

build:
	docker build -t pbpdata:latest .

nginx:
	docker run --rm --name my-nginx -v `/bin/pwd`/etc/nginx.conf:/etc/nginx/nginx.conf:ro -p 8080:80 nginx:stable

run:
	docker run --rm --network host --name django-pbpdata --env DATABASE_URL --env PGUSER --env PGPASSWORD  pbpdata:latest
