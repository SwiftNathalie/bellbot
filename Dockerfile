FROM python:3.11

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY .env .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . .

WORKDIR /app

CMD ["python", "-m", "bot"]