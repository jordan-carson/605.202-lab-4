FROM python:3.9-slim
ENV WORKDIR=/usr
WORKDIR $WORKDIR
COPY app poetry.lock pyproject.toml requirements.txt $WORKDIR/

RUN pip install --upgrade pip --no-cache-dir && \
     pip install poetry --no-cache-dir && \
     poetry run pip install -r requirements.txt

CMD python -m main