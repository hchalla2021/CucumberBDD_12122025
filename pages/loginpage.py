from pages.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    LOGIN_BUTTON = (By.NAME, "login")


    def __init__(self, driver):
        super().__init__(driver)

    def is_logibPage_loaded(self):
        return self.is_element_present(self.USERNAME_INPUT) and self.is_element_present(self.PASSWORD_INPUT) and self.is_element_present(self.LOGIN_BUTTON)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)    

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
