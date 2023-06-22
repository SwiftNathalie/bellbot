FROM python:3.11
RUN mkdir /app
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /app/
RUN poetry install -n --no-root --no-dev

# poetry dependencies installed, here you may want to copy your project package, set command for container, etc.
# all dependencies was installed without virtualenv, so you don't have to use `poetry run` in container
COPY . /app/bellbot