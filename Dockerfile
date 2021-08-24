FROM python:3.9.6-slim-buster

# poetry version
ENV POETRY_VERSION=1.0.0

WORKDIR /src

# install poetry
RUN pip install "poetry==${POETRY_VERSION}"

# copy the poetry files
COPY poetry.lock pyproject.toml ./

# export from poetry a requirements.txt and run it
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--chdir", "./src", "--bind", "0.0.0.0:8000", "app:app"]