from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def open(self, browser, page_url):
        return browser.get(page_url)

    def get_current_url(self, browser):
        return browser.current_url

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


