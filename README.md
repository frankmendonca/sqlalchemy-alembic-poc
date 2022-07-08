# SQLAlchemy + Alembic

## Init Project

```sh
$ python3 -m venv .venv
```

## Doc

https://docs.sqlalchemy.org/en/14/index.html
https://docs.sqlalchemy.org/en/14/orm/quickstart.html
https://docs.sqlalchemy.org/en/14/orm/queryguide.html
https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html

https://alembic.sqlalchemy.org/en/latest/tutorial.html
https://alembic.sqlalchemy.org/en/latest/autogenerate.html

## Tabela de Controle

|Tabela         |Coluna     |
|---------------|-----------|
|alembic_version|version_num|

## Criação de um novo Model

1. Criar classe em `models/` herdendo de `models/base.py`.
2. Adicionar a nova classe no `models/__init__.py`.

## Criar uma Revisão a partir do Model

```sh
$ alembic revision --autogenerate
```

Usando o Makefile:

```sh
$ make db-migrate
```

## Upgrade - Atualizar o ambiente

### Tudo desde a última alteração

```sh
$ alembic upgrade head
```

Usando o Makefile:

```sh
$ make db-upgrade
```

### Upgrade parcial

Se a revisão for "ae1027a6acf" pode ser rodado o comando:

```sh
$ alembic upgrade ae1
```

### Upgrade parcial (relativo)

```sh
$ alembic upgrade +2
```

## Downgrade - Rollback no ambiente (desde o começo)

```sh
$ alembic downgrade base
```

Usando o Makefile:

```sh
$ make db-downgrade
```

## Downgrade - Rollback no ambiente (somente da última revisão)

```sh
$ alembic downgrade -1
```

Usando o Makefile:

```sh
$ make db-downgrade-last
```

## Mostrar os comandos SQLs (Offline Mode)

```sh
$ alembic upgrade head --sql
```

```sh
$ alembic downgrade head:base --sql
```
