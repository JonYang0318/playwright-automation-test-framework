# Playwright Automation Test Framework



# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Playwright | Web UI Automation |
| Pytest | Test Framework |
| Page Object Model (POM) | Test Maintainability |
| Requests | API Automation Testing |
| k6 | Performance & Load Testing |
| Allure Report | Test Report |
| pytest-html | HTML Test Report |
| pytest-rerunfailures | Retry Mechanism |
| Docker | Test Environment |
| GitHub Actions | CI/CD Pipeline |
| Git | Version Control |
| FastAPI | Mock API Server |

---

# Project Structure

```
playwright-automation-test-framework

├── api
│   ├── clients
│   ├── schemas
│   └── tests
│
├── pages
│   ├── auth
│   ├── login
│   ├── finish
│   ├── inventory
│   ├── cart
│   └── checkout
│
├── tests
│   ├── cart
│   ├── checkout
│   ├── finish
│   ├── inventory
│   ├── login
|   ├── negative
│   ├── retry
│   ├── conftest.py
│   └── test_fail_screenshot.py
│
├── data
│   └── login_data.json
│
├── performance
│   └── k6
│   │     └── api_stress_test.js
│   │     └── login_load_test.js
│   │     └── scenarios.js
│   └── mock
│       ├── auth_server.py
│       └── requirements.txt
├── utils
│
├── docs
│   └── screenshots
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Installation 

Clone repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

# Test Execution Strategy

## Smoke Test

Core business flow validation:

- Login
- Add Product To Cart
- Checkout
- Complete Order

Run:

```bash
pytest -m smoke
```

## Regression Test
Core business flow validation:

- API Automation Tests
- Negative Tests

Run:

```bash
pytest -m Regression
```


# ▶ Run Tests

Run all tests:

```bash
pytest
```

Run UI automation tests:

```bash
pytest tests/
```

Run API automation tests:

```bash
pytest api/tests/
```

---

# 📊 Test Reports 測試報告

## Allure Report

Generate Allure test results:

```bash
pytest --alluredir=allure-results
```

Open report:

```bash
allure serve allure-results
```

---

## HTML Report

Generate HTML test report:

```bash
pytest --html=report.html --self-contained-html
```

---

# 🐳 Docker Execution

Build Docker image:

```bash
docker build -t playwright-test .
```

Run tests inside Docker:

```bash
docker run playwright-test
```

---

# CI/CD Pipeline

Implemented GitHub Actions workflows for automated testing.

## Automation Test Pipeline

The pipeline executes:

- Install Python dependencies
- Install Playwright browsers
- Run UI automation tests
- Run API automation tests
- Generate Allure reports


## Performance Test Pipeline

The pipeline executes:

- Setup FastAPI mock server
- Install k6
- Execute k6 load testing
- Validate performance thresholds


Workflow triggers:

- Push to master branch
- Pull Request to master branch

---

# ✅ Test Coverage 測試涵蓋範圍

## UI Automation Testing 介面測試

Covered scenarios:

- Login
- Product
- Inventory
- Shopping Cart
- Checkout
- Negative Testing


## API Automation Testing API接口測試

Covered scenarios:

- Login API
- Create User API
- Get User API
- Delete User API

---

## Performance Testing

Implemented API performance testing using k6.

A lightweight FastAPI mock server is created
to provide stable test endpoints during CI execution.


Covered scenarios:

### Load Testing

Simulate multiple concurrent users accessing login API.

Validation:

- HTTP status code
- Response time
- Error rate


### Stress Testing

Evaluate API behavior under increasing traffic.

Validation:

- System stability
- Response degradation
- Failure rate


### Performance Threshold

Configured k6 thresholds:

- 95% requests response time < 2 seconds
- API failure rate < 5%

CI pipeline will fail when performance requirements are not met.

#  Framework Features

✅ Page Object Model architecture  
✅ UI automation with Playwright  
✅ REST API automation testing  
✅ Data-driven testing  
✅ Retry failed test cases  
✅ Test reporting with Allure / HTML Report  
✅ Dockerized test execution  
✅ GitHub Actions CI/CD integration  
✅ Failure screenshot capture  
✅ Performance testing with k6
✅ Mock API environment for stable load testing
✅ CI performance threshold validation
---

# 📷 Screenshots 測試報告截圖

## GitHub Actions CI Pipeline
<img width="1631" height="763" alt="github_action" src="https://github.com/user-attachments/assets/0c758164-7052-4ac7-8cd6-46cdb93f5ab3" />




## Test Report
<img width="1616" height="797" alt="html_test" src="https://github.com/user-attachments/assets/53d503fb-c129-4056-b6af-44e43f75cc4b" />



