db-migrate:
	alembic revision --autogenerate -m "$1"

db-upgrade:
	alembic upgrade head

db-downgrade:
	alembic downgrade base

lint:
	black -l 80 .
