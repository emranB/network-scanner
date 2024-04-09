FROM python:3.7
RUN apt-get update && apt-get install -y vim iputils-ping

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install poetry

RUN mkdir -p /app/NetworkScanner
COPY pyproject.toml /app/NetworkScanner/

WORKDIR /app/NetworkScanner
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app/NetworkScanner
CMD ["sh", "run.sh", "/app/NetworkScanner"]
# Copy scan_results.txt and scanner.log back to host machine