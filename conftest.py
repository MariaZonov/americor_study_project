import allure
import pytest


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from storage.urls import BaseUrls


def pytest_addoption(parser):
    """Функция для добавления параметров при запуске тестов в командной строке"""
    parser.addoption("--url", default=BaseUrls.COMON_UI_URL, action="store")
    parser.addoption("--run_local", default=False, action="store")
    parser.addoption(
        "--incognito", action="store_true", default=False, help="Запуск в режиме инкогнито"
    )
    parser.addoption(
        "--ignore-cert", action="store_true", default=False, help="Игнорировать ошибки сертификатов"
    )
    parser.addoption(
        "--disable-cache", action="store_true", default=False, help="Отключить кэширование"
    )
    parser.addoption(
        "--disable-extensions", action="store_true", default=False, help="Отключить расширения браузера"
    )
    parser.addoption(
        "--disable-notifications", action="store_true", default=False, help="Отключить всплывающие уведомления"
    )
    parser.addoption(
        "--window-size", default="1920,1080", help="Задать размер окна браузера (ширина,высота)"
    )


@pytest.fixture(scope="function")
def browser(request):
    """Функция-фикстура для работы с браузером"""
    options = webdriver.ChromeOptions()

    additional_option = request.param.get("additional_option", None)
    if additional_option:
        options.add_argument(additional_option)

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get(BaseUrls.COMON_UI_URL)
    yield browser
    allure.attach(browser.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
    browser.quit()
