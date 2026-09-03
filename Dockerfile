FROM mcr.microsoft.com/playwright/python:v1.62.0-jammy

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p artifacts/reports artifacts/screenshots

CMD ["python", "scripts/run_e2e.py"]
