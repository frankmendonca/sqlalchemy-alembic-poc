db-migrate:
	alembic revision --autogenerate -m "$1"

db-upgrade:
	alembic upgrade head

db-downgrade:
	alembic downgrade base

db-downgrade-last:
	alembic downgrade -1

lint:
	black -l 80 .
