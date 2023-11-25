from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\iFrameTest.html")
driver.maximize_window()
print(driver.find_element(By.TAG_NAME, "h1").text)

driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
print(driver.find_element(By.TAG_NAME, "h1").text)

driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)
