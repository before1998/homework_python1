from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Находим поле ввода с названием custname и вводим имя
    driver.find_element(By.NAME, "custname").send_keys("TestUser")
    
    # Находим кнопку Submit и нажимаем на нее
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Проверяем, что после нажатия URL изменился
    assert driver.current_url != "https://httpbin.qa-territory.online/forms/post"

    driver.quit()