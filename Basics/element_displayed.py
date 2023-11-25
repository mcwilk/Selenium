from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Test.html")

hidden_element = driver.find_element(By.TAG_NAME, "p")

if hidden_element.is_displayed():
    print(hidden_element.text)

else:
    print(hidden_element.get_attribute("textContent"))
