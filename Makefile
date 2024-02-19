.PHONY: install
install:
	poetry install --no-root

.PHONY: migrate
migrate:
		poetry run python -m manage migrate

.PHONY: migrations
migrations:
	poetry run python -m manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m manage createsuperuser

.PHONY: runserver
runserver:
	poetry run python -m manage runserver

.PHONY: update
update: install migrate ;

.PHONY: worker
worker: 
	celery -A core worker --loglevel=INFO



