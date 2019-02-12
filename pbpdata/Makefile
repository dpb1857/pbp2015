

help:
	@echo "Targets:"
	@echo "  make build"

build:
	docker build -t pbpdata:latest .	

run:
	docker run --rm --network host --name pbpdata pbpdata:latest
