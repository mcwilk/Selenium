from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_login_passed():
    # ARRANGE
    options = webdriver.ChromeOptions()
    options.add_argument("start_maximized")
    # options.add_experimental_option("detach", True)
    chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)

    # ACT
    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("autotester123@gmail.com")

    # Optional: if "password" element is not clickable
    # driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "password"))

    driver.find_element(By.ID, "password").send_keys("autotester123")

    # Optional 2: instead of clicking on "Login" button
    # driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    driver.find_element(By.NAME, "login").click()

    # ASSERT
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()


def test_login_failed():
    # ARRANGE
    options = webdriver.ChromeOptions()
    options.add_argument("start_maximized")
    # options.add_experimental_option("detach", True)
    chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)

    # ACT
    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("autotester123@gmail.com")

    # Optional: if "password" element is not clickable
    # driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "password"))

    driver.find_element(By.ID, "password").send_keys("autotesterXYZ")

    # Optional 2: instead of clicking on "Login" button
    # driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    driver.find_element(By.NAME, "login").click()

    # ASSERT
    assert "ERROR: Incorrect username or password" in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
