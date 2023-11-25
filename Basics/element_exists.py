from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Test.html")

# Option 1
elements = driver.find_elements(By.TAG_NAME, "p")  # returns List

if len(elements) > 0:
    print("Element exists!")

else:
    print("Element does not exist!")

# Option 2
try:
    driver.find_element(By.TAG_NAME, "ppp")

except NoSuchElementException:
    print("Element does not exist!")

else:
    print("Element exists!")
