import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# Detaches browser from the execution (it is not closed at the end)
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)

start = time.time()
driver.implicitly_wait(7)

driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Waits2.html")
driver.maximize_window()

try:
    driver.find_element(By.ID, "clickOnMe").click()
    # driver.find_element(By.ID, "clickOnMe12345").click()
    print(driver.find_element(By.TAG_NAME, "p").text)

except NoSuchElementException:
    print("Exception occurred!")

finally:
    print(time.time() - start)
