from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Test.html")

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox.click()

if checkbox.is_selected():
    print("Selected!")
    checkbox.click()

else:
    print("Not selected!")
    checkbox.click()
