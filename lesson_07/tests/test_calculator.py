from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_calculator():
    # 1. Создание и настройка драйвера
    driver = webdriver.Chrome()

    try:
        # 2. Создание объекта страницы
        calc_page = CalculatorPage(driver)

        # 3. Выполнение действий строго через методы Page Object
        calc_page.open()
        calc_page.set_delay(45)
        calc_page.click_7()
        calc_page.click_plus()
        calc_page.click_8()
        calc_page.click_equals()

        # 4. Ожидание появления результата
        calc_page.wait_for_result("15", timeout=60)
        result = calc_page.get_result()
    finally:
        # 5. Закрытие драйвера
        driver.quit()

    # 6. Проверка результата (assert только в коде теста)
    assert result == "15", f"Ожидалось 15, но получено {result}"
