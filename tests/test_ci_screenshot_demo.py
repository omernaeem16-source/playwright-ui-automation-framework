def test_ci_failure_screenshot(page):
    # Open the demo website
    page.goto("https://qademo.com")

    # Deliberately fail this test
    assert False, "Testing screenshot capture in GitHub Actions"