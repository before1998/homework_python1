from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        # 1. Откройте страницу
        driver.get("https://gitflic.ru/")

        # 2. Установите cookie пользователя 1
        # ЗАМЕНИТЕ значения на реальные данные из браузера!
        user1_cookie = {
            "name": "SESSION",
            "value": "ZDhjNWY4N2MtZTY5MS00MzAwLWJmNjQtOGFkNzMwOTg0OGY0",
            "domain": ".gitflic.ru"
        }
        driver.add_cookie(user1_cookie)

        # 3. Обновите страницу для применения cookie
        driver.refresh()

        # 4. Перейдите на страницу пользователя 1
        # Замените 'username1' на реальный логин
        driver.get("https://gitflic.ru/user/before1")

        # 5. Сохраните текущий URL
        url_user1 = driver.current_url

        # 6. Разлогиньтесь (очистите куки)
        driver.delete_all_cookies()

        # 7. Установите cookie пользователя 2
        # Замените значение value на реальные данные
        user2_cookie = {
            "name": "SESSION",
            "value": "OGUwNDhmMWQtYmE3OS00MDk2LWJiNjAtNzBhMTBmOGRmZWUy",
            "domain": ".gitflic.ru"
        }
        driver.add_cookie(user2_cookie)

        # 8. Обновите страницу для применения cookie
        driver.refresh()

        # 9. Перейдите на страницу пользователя 2
        # Замените 'username2' на реальный логин
        driver.get("https://gitflic.ru/user/before2")

        # 10. Сохраните текущий URL
        url_user2 = driver.current_url

        # 11. Проверьте, что URL различаются
        assert url_user1 != url_user2, (
            "URL профилей пользователей должны различаться"
        )
    finally:
        driver.quit()
