from urllib.parse import unquote

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    visibility_of_any_elements_located,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from storage.urls import BaseUrls


class BasePage:
    def open(self, browser, page_url):
        return browser.get(page_url)

    def get_current_url(self, browser):
        return browser.current_url

    def check_url_changes(self, browser, page_url, time_wait=10):
        """Ожидает до 10 секунд, пока URL не изменится по сравнению с page_url"""
        try:
            WebDriverWait(browser, time_wait).until(EC.url_changes(page_url))
        except TimeoutException:
            raise TimeoutException(f"URL не изменился - текущий URL {page_url}")

    def wait_and_switch_to_window(self, browser, window_handles=1, num_windows=2, time_wait=10):
        """
        Ожидает, пока количество окон не станет равным num_windows
        Переключает на окно по индексу window_handles
        Если указанного индекса нет в списке окон, выбрасывается исключение
        """
        try:
            WebDriverWait(browser, time_wait).until(EC.number_of_windows_to_be(num_windows))
            browser.switch_to.window(browser.window_handles[window_handles])
        except (TimeoutException, IndexError) as e:
            raise Exception("Не удалось переключиться на вкладку: " + str(e))

    def element_is_visible(self, browser, method, css_selector, description, time_wait=10, displayed=False):
        wait = WebDriverWait(browser, time_wait)
        try:
            return wait.until(visibility_of_element_located((method, css_selector)))
        except TimeoutException:
            if displayed:
                return False
            raise TimeoutException(f"Элемент вэб-страницы {description} не найден")

    def find_element(self, browser, method, css_selector, description, check_visibility=True, time_wait=10):
        if check_visibility:
            self.element_is_visible(browser, method, css_selector, description, time_wait)
        return browser.find_element(method, css_selector)

    def elements_is_visible(self, browser, method, css_selector, description, time_wait=10):
        wait = WebDriverWait(browser, time_wait)
        try:
            return wait.until(visibility_of_any_elements_located((method, css_selector)))
        except TimeoutException:
            raise TimeoutException(f"Элементы вэб-страницы {description} не найдены")

    def find_elements(self, browser, method, css_selector, description, check_visibility=True):
        if check_visibility:
            self.elements_is_visible(browser, method, css_selector, description)
        return browser.find_elements(method, css_selector)

    def decode_url(self, url):
        """Декодирует закодированную часть URL"""
        if "#" in url:
            base_url, encoded_part = url.split("#", 1)
            decoded_part = unquote(encoded_part)
            return f"{base_url}#{decoded_part}"
        return url

    def scroll_to_element(self, browser, element):
        """Прокручивает страницу до элемента"""
        browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    def scroll_and_click(self, browser, element):
        """Скроллит страницу до элемента и кликает"""
        self.scroll_to_element(browser, element)
        element.click()

    def open_new_window_by_url(self, browser, url=BaseUrls.AMERICOR_UI_URL):
        """Открывает новую вкладку по заданому URL"""
        browser.execute_script(f"window.open('{url}')")
