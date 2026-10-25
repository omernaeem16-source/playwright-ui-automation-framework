
import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

load_dotenv()


# Capture a screenshot when a test fails during its call phase.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only capture screenshots for failed test execution.
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            # Create the screenshots folder if it does not exist.
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            # Build a filename using the test name.
            screenshot_name = item.name.replace("[", "_").replace("]", "")
            screenshot_path = screenshot_dir / f"{screenshot_name}.png"

            # Save the screenshot for debugging.
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"\nFailure screenshot saved: {screenshot_path}")
