import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from class_for_explicit_wait import WaitForListSize


options = webdriver.ChromeOptions()
# Detaches browser from the execution (it is not closed at the end)
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)

start = time.time()
wait = WebDriverWait(driver, 7)

driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Waits2.html")
driver.maximize_window()

driver.find_element(By.ID, "clickOnMe").click()

# lambda approach
try:
    wait.until(lambda x: len(x.find_elements(By.TAG_NAME, "p")) == 1)  # our lambda with condition to be met
    print(driver.find_element(By.TAG_NAME, "p").text)

except TimeoutException:
    print("TimeoutException occurred!")

finally:
    print(time.time() - start)

# class approach
# try:
#     wait.until(WaitForListSize("//p", 1))  # our class instance with condition to be met
#     print(driver.find_element(By.TAG_NAME, "p").text)
#
# except TimeoutException:
#     print("TimeoutException occurred!")
#
# finally:
#     print(time.time() - start)
