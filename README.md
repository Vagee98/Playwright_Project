# Playwright Python Automation Framework
## Overview
This project is an automation testing framework developed using Playwright, Python, and Pytest.

The framework automates key OrangeHRM business workflows and follows industry-standard automation design principles such as Page Object Model (POM), Data-Driven Testing, and Pytest Fixtures.

## Features
- Login Automation
- Data-Driven Testing using JSON
- Multiple User Login Validation
- Add Employee Workflow
- Search Employee Workflow
- Logout Functionality
- Screenshot Capture
- HTML Reporting
- Page Object Model (POM)
- Pytest Fixtures
- Git Version Control
- GitHub Repository Integration

## Technologies Used
- Python
- Playwright
- Pytest
- JSON
- Git
- GitHub
- pytest-html

## Framework Components
### Page Object Model (POM)
Page classes are separated from test scripts to improve maintainability and reusability.

### Data-Driven Testing
Test data is maintained in JSON files and executed using Pytest parameterization.

### Fixtures
Pytest fixtures are used for browser initialization and reusable setup operations.

### Reports
HTML reports are generated using pytest-html.

### Screenshots
Screenshots are captured during test execution for validation and debugging purposes.

## Project Structure

```text
Playwright_Project/
│
├── data/
│   ├── login_data.json
│   └── employee_data.json
│
├── pages/
│   ├── login_page.py
│   ├── pim_page.py
│   └── logout_page.py
│
├── reports/
│
├── screenshots/
│
├── tests/
│   ├── test_login.py
│   ├── test_add_employee.py
│   ├── test_search_employee.py
│   └── test_logout.py
│
├── conftest.py
└── README.md
```
## Test Scenarios Automated
### Login
- Valid Login
- Multiple User Login Validation

### Employee Management
- Navigate to PIM
- Add Employee
- Search Employee

### Session Management
- User Logout

## Running the Tests
Execute all tests:
```bash
pytest

Execute a specific test:
```bash
pytest tests/test_ui_independent_flow.py
```

Execute in verbose mode:
```bash
pytest -v
```

## Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

Generated report:
```text
reports/report.html
```

## Screenshots
Screenshots are stored in:

```text
screenshots/
```
These screenshots help in validating execution results and debugging failures.

## Git Commands Used
Initialize Repository:
```bash
git init
```
Add Files:
```bash
git add .
```
Commit Changes:
```bash
git commit -m "commit message"
```
Push Changes:
```bash
git push
```

## Future Enhancements
- CI/CD Integration using GitHub Actions
- API Testing Integration
- UI + API Hybrid Framework
- Storage State Authentication
- Parallel Execution
- Cross Browser Execution

## Author

Vageesha BS

Playwright | Python | Pytest | Automation Testing
