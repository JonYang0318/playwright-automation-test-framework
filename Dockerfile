FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p artifacts/reports artifacts/screenshots

CMD ["python", "-m", "pytest", "tests/e2e/test_parabank.py", "--html=artifacts/reports/pytest-report.html", "--self-contained-html", "--junitxml=artifacts/reports/junit.xml", "--tb=short"]
