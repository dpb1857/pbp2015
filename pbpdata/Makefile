

help:
	@echo "Targets:"
	@echo "  make build"

build:
	docker build -t pbpdata:latest .

nginx:
	# docker run --rm --name my-nginx -v `/bin/pwd`/static:/usr/share/nginx/html/static:ro -p 8080:80 nginx:stable
	docker run --rm --name my-nginx -v `/bin/pwd`/etc/nginx.conf:/etc/nginx/nginx.conf:ro -p 8080:80 nginx:stable

run:
	docker run --rm --network host --name django-pbpdata pbpdata:latest
