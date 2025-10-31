# ----- Estágio 1: Builder -----
FROM python:3.12 AS builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt -t /app/venv

COPY . .


# ----- Estágio 2: Imagem Final -----
FROM python:3.12-slim

WORKDIR /app

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

COPY --from=builder /app/venv /app/venv
COPY --from=builder /app /app

ENV PATH="/app/venv/bin:$PATH" \
    PYTHONPATH="/app/venv"

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]