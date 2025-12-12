from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
      return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def select_from_dropdown_by_visible_text(self, locator, text):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def takescreenshot(self, file_path):
       os.makedirs(os.path.dirname(file_path), exist_ok=True)
       self.driver.save_screenshot(file_path)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False   