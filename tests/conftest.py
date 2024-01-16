import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

def seleniod_browser()

@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )


    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()