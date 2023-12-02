import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_create_account_failed():
    # ARRANGE
    options = webdriver.ChromeOptions()
    options.add_argument("start_maximized")
    # options.add_experimental_option("detach", True)
    chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)

    # ACT
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("autotester123@gmail.com")
    driver.find_element(By.ID, "reg_password").send_keys("autotester123")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)

    # ASSERT
    assert "Error: An account is already registered" in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text


def test_create_account_passed():
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

    # ASSERT
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
