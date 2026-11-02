from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    total_cost = ""
    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Ожидание загрузки списка товаров
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        # Добавление товаров в корзину
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Нажатие кнопки Checkout
        driver.find_element(By.ID, "checkout").click()

        # Заполнение формы данными
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Нажатие кнопки Continue
        driver.find_element(By.ID, "continue").click()

        # Чтение итоговой стоимости со страницы
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_element = driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        total_cost = total_element.text

        # Закрытие браузера (проверка идет после закрытия по заданию)
        driver.quit()

        # Проверка итоговой суммы
        assert "$58.29" in total_cost, (
            f"Ожидалась сумма '$58.29', получено '{total_cost}'"
        )

    except Exception as e:
        driver.quit()
        raise e
