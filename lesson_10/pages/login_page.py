from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    """Класс для взаимодействия со страницей авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.
        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self._username_locator = (By.ID, "user-name")
        self._password_locator = (By.ID, "password")
        self._login_button_locator = (By.ID, "login-button")

    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя в поле логина.
        :param username: Строка с именем пользователя.
        """
        self.driver.find_element(*self._username_locator).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввод пароля в поле пароля.
        :param password: Строка с паролем.
        """
        self.driver.find_element(*self._password_locator).send_keys(password)

    def click_login_button(self) -> None:
        """Нажатие на кнопку входа в систему."""
        self.driver.find_element(*self._login_button_locator).click()

    def get_error_message(self) -> str:
        """
        Получение текста сообщения об ошибке.
        :return: Строка с текстом ошибки.
        """
        element: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, ".error-message-container"
        )
        return element.text
