# Diplom3 - Automated Testing Project

This project contains automated tests for the Stellar Burgers web application using Selenium WebDriver and Python.

## Project Structure

- `conftest.py` - Contains pytest fixtures and configuration
- `locators/` - Contains locator classes for page elements
- `pages/` - Contains page object classes
- `tests/` - Contains test files
- `screenshots/` - Contains screenshots taken during test failures
- `allure-report/` - Contains Allure test reports

## Running Tests

To run the tests, use the following command:

```bash
pytest tests/
```

To generate an Allure report:

```bash
pytest tests/ --alluredir=allure-results
allure generate allure-results --clean -o allure-report
```

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Allure Report
