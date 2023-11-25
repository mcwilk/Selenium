from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Test.html")

first_name_input = driver.find_element(By.ID, "fname")

if first_name_input.is_enabled():
    first_name_input.send_keys("ABCDEFGH")

else:
    print("Element is disabled")
