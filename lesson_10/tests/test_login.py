import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from lesson_10.pages.login_page import LoginPage


@allure.feature("Авторизация пользователя")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:

    @pytest.fixture(scope="function")
    def driver(self) -> WebDriver:
        """Фикстура для инициализации и закрытия браузера."""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    @allure.title("Успешная авторизация стандартного пользователя")
    @allure.description(
        "Проверка возможности успешного входа в систему с "
        "валидными учетными данными стандартного пользователя."
    )
    def test_successful_login(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Ввести валидные учетные данные"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")

        with allure.step("Нажать кнопку 'Login'"):
            login_page.click_login_button()

        with allure.step("Проверить успешный переход на страницу товаров"):
            assert "inventory.html" in driver.current_url, (
                "Редирект на страницу инвентаря не произошел"
            )

    @allure.title("Ошибка при вводе невалидного пароля")
    @allure.description(
        "Проверка отображения сообщения об ошибке при вводе "
        "неверного пароля."
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_password(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Ввести имя пользователя и неверный пароль"):
            login_page.enter_username("standard_user")
            login_page.enter_password("wrong_password")
            login_page.click_login_button()

        with allure.step("Проверить наличие сообщения об ошибке"):
            error_text = login_page.get_error_message()
            expected_msg = (
                "Epic sadface: Username and password do not match"
            )
            assert expected_msg in error_text, (
                "Сообщение об ошибке не совпадает с ожидаемым"
            )
