from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage


class MainShopPage(BasePage):
    CART_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BOLT_TSHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    CART_ONESIE_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.click(self.CART_BACKPACK_BTN)

    def add_bolt_tshirt_to_cart(self):
        self.click(self.CART_BOLT_TSHIRT_BTN)

    def add_onesie_to_cart(self):
        self.click(self.CART_ONESIE_BTN)

    def go_to_cart(self):
        self.click(self.CART_LINK)
        return CartPage(self.driver)
