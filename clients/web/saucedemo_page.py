from selenium.webdriver.common.by import By
from clients.web.base_page import BasePage
from storage.credentials import SAUCEDEMO_LOGIN, SAUCEDEMO_PASSWORD

class SauceDemoPage(BasePage):
    LOGIN_FIELD = (By.CSS_SELECTOR,"#user-name","логин",)
    PASSWORD_FIELD = (By.CSS_SELECTOR,"#password","пароль",)
    LOGIN_BUTTON = (By.CSS_SELECTOR,"#login-button","кнопка для входа",)

    def fill_in_login_in_field(self, browser):
        login_field = self.find_element(browser, *self.LOGIN_FIELD)
        login_field.send_keys(SAUCEDEMO_LOGIN)

    def fill_in_password_in_field(self, browser):
        password_field = self.find_element(browser, *self.PASSWORD_FIELD)
        password_field.send_keys(SAUCEDEMO_PASSWORD)

    def click_to_login_button(self, browser):
        login_button = self.find_element(browser, *self.LOGIN_BUTTON)
        login_button.click()





