import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        hello_world_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        screenshot_path = os.path.join(
            os.getcwd(), "dynamic_loading_screenshot.png"
        )
        driver.save_screenshot(screenshot_path)

        expected_text = "Hello World!"
        assert hello_world_element.text == expected_text, (
            f"Ожидался '{expected_text}', "
            f"получен: '{hello_world_element.text}'"
        )
    finally:
        driver.quit()
