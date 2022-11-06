FROM python:3.9-slim

WORKDIR /usr

COPY poetry.lock ./
COPY pyproject.toml ./

RUN pip install --upgrade pip --no-cache-dir
RUN pip install poetry --no-cache-dir
RUN poetry install -v --no-cache

COPY app ./

CMD python -m app.main