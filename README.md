# Solution

For Solution checkout [implementation.md](implementation.md)


## Running the application

```bash
docker compose up --build
```

There are two containers running:

1. web: This is the Django application container.
2. worker: This is the Django worker container. Which handles the background tasks for sending emails.

You can run each of them without the docker file as well:

```bash
python manage.py runserver 0.0.0.0:8000
python manage.py process_tasks
```
But for this application, I would recommend using the docker file as it will handle the dependencies and the database. Otherwise install poetry, install dependencies and run the migrations:

# Install poetry

```bash
pip install poetry
poetry install
python manage.py migrate
```


