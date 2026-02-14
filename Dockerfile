FROM python:3.14.3

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser && chown -R appuser:appuser /app

COPY --chown=appuser:appuser . .

USER appuser
CMD ["python", "main.py"]