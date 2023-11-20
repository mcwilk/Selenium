import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# Detaches browser from the execution (it is not closed at the end)
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)

start = time.time()
wait = WebDriverWait(driver, 7, 0.5, [NoSuchElementException])

driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Waits2.html")
driver.maximize_window()

# driver.find_element(By.ID, "clickOnMe").click()

try:
    wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "p")))
    print(driver.find_element(By.TAG_NAME, "p").text)

except TimeoutException:
    print("TimeoutException occurred!")

finally:
    print(time.time() - start)
