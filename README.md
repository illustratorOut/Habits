| Описание                 | Команды                        |
|--------------------------|--------------------------------|
| ✔️ Приминить миграции    | ```python manage.py migrate``` |
| ✔️ Создать пользователей | ```python manage.py ccsu```    |

<br>

```commandline
flake8 . --exclude=venv,env,migrations --ignore=E501
```

```commandline
celery -A config worker -l INFO
celery -A config worker --loglevel=info -P eventlet
celery -A config beat -l INFO -S django
```

```dotenv
CACHE_ENABLED=True
REDIS=redis://127.0.0.1:6379

POSTGRES_DB=
POSTGRES_PASSWORD=
POSTGRES_USER=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

TELEGRAM_TOKKEN=

CELERY_BROKER_URL=redis://redis:6379
CELERY_RESULT_BACKEND=redis://redis:6379
```