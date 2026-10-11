# Playwright UI Automation Framework

A Python-based web UI automation framework built with **Playwright and Pytest** to test essential e-commerce workflows on [QADemo](https://qademo.com/).

The project demonstrates practical experience with browser automation, Page Object Model (POM), parametrized testing, positive and negative scenarios, environment-based credentials, and end-to-end testing.

## Tech Stack

- Python
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- python-dotenv
- Git and GitHub

## Project Structure

```
playwright-ui-automation-framework/
├── pages/
│   ├── login_page.py
│   ├── catalog_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── check_out_page.py
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   ├── test_product_flow.py
│   ├── test_checkout.py
│   └── test_cart.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

The framework currently contains **12 test executions**, covering:

- Homepage verification
- Successful and unsuccessful login scenarios
- Product details and add-to-cart workflow
- End-to-end checkout and order confirmation
- Invalid payment card validation
- Checkout validation for a missing shipping address
- Removing a product from the cart
- Increasing and decreasing product quantity
- Dynamic cart subtotal calculation

## Setup

### 1. Clone the repository

```
git clone https://github.com/omernaeem16-source/playwright-ui-automation-framework.git
cd playwright-ui-automation-framework
```

### 2. Create and activate a virtual environment (recommended)

```
python -m venv .venv
```

On Windows PowerShell:

```
.\.venv\Scripts\Activate.ps1
```

On macOS / Linux:

```
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure credentials

Create a `.env` file in the project root:

```
QA_USERNAME=your_test_username
QA_PASSWORD=your_test_password
```

Use valid test credentials for the demo application. **Never commit the `.env` file or real credentials to GitHub.**

## Run Tests

Run the complete suite:

```
pytest
```

Run tests with a visible browser and slower execution:

```
pytest --headed --slowmo 300
```

Run a specific test file:

```
pytest tests/test_cart.py
```

## HTML Test Report

Generate a self-contained HTML report:

```
pytest --html=report.html --self-contained-html
```

Open `report.html` in a browser to see which tests passed or failed, along with durations and failure details.

To keep screenshots and traces for failed tests, run:

```
pytest --screenshot only-on-failure --tracing retain-on-failure
```

The files are saved in the `test-results/` folder.

## Design Approach

- **Page Object Model:** Separates page locators and actions from test logic.
- **Reusable fixtures:** Uses Pytest and Playwright fixtures for browser test execution.
- **Parametrization:** Runs login scenarios with different credentials.
- **Assertions:** Verifies page navigation, product information, cart quantity, subtotal, and validation messages.
- **Environment variables:** Keeps credentials outside the test source code.

## Current Test Results

Latest complete test run:

- **12 passed**
- **0 failed**
- **Execution time:** 44.83 seconds

## Future Improvements

- Add CI/CD integration with GitHub Actions.
- Expand test coverage where useful.
- Embed failure screenshots directly in the HTML report.
