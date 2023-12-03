import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_update_billing_address():
    # ARRANGE
    options = webdriver.ChromeOptions()
    options.add_argument("start_maximized")
    # options.add_experimental_option("detach", True)
    chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)

    suffix = str(random.randint(1, 10000))

    # ACT
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(f"autotester{suffix}@gmail.com")
    driver.find_element(By.ID, "reg_password").send_keys("autotester123")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Andreas")
    driver.find_element(By.ID, "billing_last_name").send_keys("Doe")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("Niepodleglosci 1")
    driver.find_element(By.ID, "billing_postcode").send_keys("00-001")
    driver.find_element(By.ID, "billing_city").send_keys("Cracow")
    driver.find_element(By.ID, "billing_phone").send_keys("111222333")
    driver.find_element(By.XPATH, "//button[@value='Save address']").click()

    # ASSERT
    assert driver.find_element(By.XPATH, "//div[@class='woocommerce-message']").text == "Address changed successfully."

