# ── Stage 1: Builder ──────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Stage 2: Production ───────────────────────────
FROM python:3.11-slim AS production

WORKDIR /app

# Copy installed packages from builder to system location
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Copy application code
COPY app/ .

ENV APP_VERSION=1.0.0
ENV APP_ENV=production

# Non-root user
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
