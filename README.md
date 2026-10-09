# Playwright UI Automation Framework

A Python-based web UI automation framework built with **Playwright and Pytest** to test essential e-commerce workflows on [QADemo](https://qademo.com/).

The project demonstrates practical experience with browser automation, Page Object Model (POM), parametrized testing, positive and negative scenarios, environment-based credentials, and end-to-end testing.

## Tech Stack

* Python
* Playwright
* Pytest
* pytest-playwright
* python-dotenv
* Git and GitHub

## Project Structure

```text
playwright-nopcommerce-automation/
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
├── test_data/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

The framework currently contains **12 test executions**, covering:

* Homepage verification
* Successful and unsuccessful login scenarios
* Product details and add-to-cart workflow
* End-to-end checkout and order confirmation
* Invalid payment card validation
* Checkout validation for a missing shipping address
* Removing a product from the cart
* Increasing and decreasing product quantity
* Dynamic cart subtotal calculation

## Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd playwright-nopcommerce-automation
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual repository URL.

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure credentials

Create a `.env` file in the project root:

```text
QA_USERNAME=your_test_username
QA_PASSWORD=your_test_password
```

Use valid test credentials for the demo application. **Never commit the `.env` file or real credentials to GitHub.**

## Run Tests

Run the complete suite:

```bash
pytest
```

Run tests with a visible browser and slower execution:

```bash
pytest --headed --slowmo 300
```

Run a specific test file:

```bash
pytest tests/test_cart.py
```

## Design Approach

* **Page Object Model:** Separates page locators and actions from test logic.
* **Reusable fixtures:** Uses Pytest and Playwright fixtures for browser test execution.
* **Parametrization:** Runs login scenarios with different credentials.
* **Assertions:** Verifies page navigation, product information, cart quantity, subtotal, and validation messages.
* **Environment variables:** Keeps credentials outside the test source code.

## Current Test Results

Latest complete test run:

* **12 passed**
* **0 failed**
* **Execution time:** 44.83 seconds

## Future Improvements

* Add CI/CD integration.
* Expand test coverage where useful.
* Improve test reporting and failure diagnostics.
