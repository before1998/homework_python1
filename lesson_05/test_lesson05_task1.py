from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    
    original_url = driver.current_url
    
    # Находим и кликаем на ссылку "HTML Form"
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    
    # Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url
    
    # Возвращаемся назад на главную страницу
    driver.back()
    
    # Проверяем, что вернулись на исходный URL (учитываем возможный слеш в конце)
    assert driver.current_url.rstrip('/') == original_url.rstrip('/')
    
    driver.quit()
    