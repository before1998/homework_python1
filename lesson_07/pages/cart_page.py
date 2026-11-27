from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)
