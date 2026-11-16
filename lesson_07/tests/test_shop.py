from selenium import webdriver
from pages.login_page import LoginPage


def test_shop_checkout():
    # 1. Создание и настройка драйвера
    driver = webdriver.Firefox()

    try:
        # 2. Создание объекта страницы и открытие сайта
        login_page = LoginPage(driver)
        login_page.open()

        # 3. Авторизация
        main_page = login_page.login("standard_user", "secret_sauce")

        # 4. Добавление товаров в корзину
        main_page.add_backpack_to_cart()
        main_page.add_bolt_tshirt_to_cart()
        main_page.add_onesie_to_cart()

        # 5. Переход в корзину
        cart_page = main_page.go_to_cart()

        # 6. Нажатие кнопки Checkout
        checkout_page = cart_page.click_checkout()

        # 7. Заполнение формы данными
        checkout_page.fill_checkout_info("Ivan", "Ivanov", "12345")

        # 8. Чтение итоговой стоимости со страницы
        total_cost = checkout_page.get_total_cost()
    finally:
        # 9. Закрытие браузера
        driver.quit()

    # 10. Проверка результата (assert только в коде теста)
    assert "$58.29" in total_cost, (
        f"Ожидалась сумма $58.29, но получено: {total_cost}"
    )
