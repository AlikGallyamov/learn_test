from selene import browser
import pytest
import secret_values


@pytest.fixture
def open_browser():
    browser.config.window_height = 1690
    browser.config.window_width = 1080
    browser.open(secret_values.url)
    yield
    browser.quit()
