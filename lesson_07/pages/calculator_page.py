from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class CalculatorPage(BasePage):
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    BTN_7 = (By.XPATH, "//span[text()='7']")
    BTN_PLUS = (By.XPATH, "//span[text()='+']")
    BTN_8 = (By.XPATH, "//span[text()='8']")
    BTN_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CSS_SELECTOR, "div.screen")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, delay):
        element = self.find_element(self.DELAY_INPUT)
        element.clear()
        element.send_keys(str(delay))

    def click_7(self):
        self.click(self.BTN_7)

    def click_plus(self):
        self.click(self.BTN_PLUS)

    def click_8(self):
        self.click(self.BTN_8)

    def click_equals(self):
        self.click(self.BTN_EQUALS)

    def _check_result(self, expected_result):
        return self.find_element(
            self.RESULT_SCREEN
        ).text.strip() == str(expected_result)

    def wait_for_result(self, expected_result, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            lambda d: self._check_result(expected_result)
        )

    def get_result(self):
        return self.find_element(self.RESULT_SCREEN).text.strip()
