import allure
import pytest

from clients.web.americor.main_page import MainPage
from storage.urls import BaseUrls


@pytest.mark.americor_ui_main_page
@allure.feature("Главная страница")
class TestMainPage:

    @allure.title("Переход на главную страницу")
    @pytest.mark.parametrize("browser", [
        {"additional_option": "--incognito"},
        {"additional_option": "--ignore-cert"},
        {"additional_option": "--disable-cache"},
        {"additional_option": "--disable-extensions"},
        {"additional_option": "--disable-notifications"},
        {"additional_option": "--window-size"},
    ], indirect=True)
    def test_go_to_main_page(self, browser):
        with allure.step("Шаг: Перейти на главную страницу"):
            MainPage().open(browser, BaseUrls.AMERICOR_UI_URL)
        with allure.step("Проверка: Открылся каталог стратегий"):
            assert BaseUrls.AMERICOR_UI_URL in MainPage().get_current_url(browser), "Открылась не та страница"
