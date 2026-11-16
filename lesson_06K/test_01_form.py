import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form():
    if sys.platform == "darwin":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Edge()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "data-types.html"
        )

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        wait = WebDriverWait(driver, 5)

        zip_code = driver.find_element(By.NAME, "zip-code")
        wait.until(
            lambda d: "is-invalid" in zip_code.get_attribute("class")
            or "invalid" in zip_code.get_attribute("class")
        )
        assert (
            "is-invalid" in zip_code.get_attribute("class")
            or "invalid" in zip_code.get_attribute("class")
        ), "Поле Zip code должно быть подсвечено красным"

        fields = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]
        for field_name in fields:
            field = driver.find_element(By.NAME, field_name)
            wait.until(
                lambda d: "is-valid" in field.get_attribute("class")
                or "valid" in field.get_attribute("class")
            )
            assert (
                "is-valid" in field.get_attribute("class")
                or "valid" in field.get_attribute("class")
            ), f"Поле {field_name} должно быть подсвечено зеленым"

    finally:
        driver.quit()
