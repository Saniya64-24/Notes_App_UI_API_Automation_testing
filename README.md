# Notes_App_UI_API_Automation

# Open Source Quality Intelligence - Pytest

A Selenium + Python + Pytest hybrid automation framework for the ExpandTesting Notes App covering UI, API, E2E testing, parallel execution, CI/CD and reporting.

## Project Overview

- UI: https://practice.expandtesting.com/notes/app
- API: https://practice.expandtesting.com/notes/api/api-docs

## Tech Stack

- Python 3.10+
- Selenium WebDriver
- Pytest + pytest-xdist + pytest-rerunfailures
- Requests library
- Allure reporting
- Jenkins CI/CD
- Docker Selenium Grid

## Project Structure
## Project Structure

```
c_Selenium_Python_Advanced_Capstone_Project/
├── api/
│   └── api_client.py
├── config/
│   ├── config.yaml
│   └── environment.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   └── notes_page.py
├── tests/
│   ├── test_login.py
│   ├── test_notes_ui.py
│   ├── test_api.py
│   └── test_e2e.py
├── utils/
│   ├── logger.py
│   └── wait_helper.py
├── docker/
│   └── docker-compose.yml
├── screenshots/
├── logs/
├── allure-results/
├── conftest.py
├── pytest.ini
├── jenkinsfile
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/Saniya64-24/Notes_App_UI_API_Automation_testing.git
cd c_Selenium_Python_Advanced_Capstone_Project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Update `config/config.yaml` with your credentials:

```yaml
base_url: "https://practice.expandtesting.com/notes/app"
api_url: "https://practice.expandtesting.com/notes/api"
username: "your-email@gmail.com"
password: "your-password"
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run only UI tests
pytest tests/test_login.py -v
pytest tests/test_notes_ui.py -v

# Run only API tests
pytest tests/test_api.py -v

# Run only E2E tests
pytest tests/test_e2e.py -v

# Run in parallel with 2 workers
pytest tests/ -n 2 -v

# Generate Allure report
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## Docker Parallel Execution

```bash
cd docker
docker-compose up -d
cd ..
pytest tests/ -n 2 -v
docker-compose down
```

## CI/CD Jenkins

Jenkins pipeline is defined in `jenkinsfile` with these stages:

1. Clone Repository
2. Check Python Version
3. Install Dependencies
4. Run API Tests
5. Generate Allure Report
6. Archive Allure Report

## Functional Requirements Covered

| Requirement | Description | Test File | Status |
|---|---|---|---|
| FR-01 | UI Login works | test_login.py | Covered |
| FR-02 | Create note via UI | test_notes_ui.py | Covered |
| FR-03 | Note appears instantly in UI | test_notes_ui.py | Covered |
| FR-04 | API GET /notes returns list | test_api.py | Covered |
| FR-05 | UI note appears in API | test_e2e.py | Covered |
| FR-06 | Delete note via API | test_api.py | Covered |
| FR-07 | Deleted note disappears from UI | test_e2e.py | Covered |
| FR-08 | API response under 2 seconds | test_api.py | Covered |
| FR-09 | Negative scenarios UI and API | test_login.py + test_api.py | Covered |

## Test Files Overview

## Test Files Overview

| File | FR Covered | What it tests |
|---|---|---|
| test_login.py | FR-01, FR-09 | Valid login, invalid login with wrong credentials (parametrized), empty fields validation, invalid email format validation |
| test_notes_ui.py | FR-02, FR-03, FR-04 | Create note with random title and description, note appears instantly in UI without page refresh, GET notes API returns list, UI page load time under 2 seconds |
| test_api.py | FR-04, FR-06, FR-08, FR-09 | GET notes returns list, API response time under 2 seconds, delete note via API and confirm removal, GET without token returns 401, delete non-existent note returns 400, create note with missing fields returns 400 |
| test_e2e.py | FR-05, FR-07 | UI created note appears in API response, API deleted note disappears from UI after refresh |

## Features

- Page Object Model design pattern
- Explicit waits using WebDriverWait
- JavaScript executor waits for DOM readiness
- Screenshot capture automatically on test failure
- Structured logging to logs/test_run.log
- Performance trend logging to logs/performance_trend.json
- Self-healing locators with fallback strategy
- Auto-retry for flaky tests using pytest-rerunfailures
- MCP integration with Claude AI for intelligent test data generation and failure analysis
- Allure reports with environment properties
- Parallel execution with pytest-xdist
- Docker Selenium Grid for distributed execution
- Jenkins CI/CD pipeline

## Deliverables

- Manual test plan with 9 scenarios and 14 test cases
- Requirement Traceability Matrix covering FR-01 to FR-09
- Selenium Python Pytest automation framework
- UI + API + E2E hybrid test suite
- Parallel execution with pytest-xdist
- Allure HTML report
- Jenkins CI/CD pipeline
- Docker Selenium Grid setup
- Performance trend log
- MCP AI integration


<!-- cd docker
docker-compose up -d
cd ..
pytest tests/ -n 2 -v

allure serve allure-results -->

