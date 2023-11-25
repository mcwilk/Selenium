from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Test.html")
driver.maximize_window()

driver.execute_script("arguments[0].click()", driver.find_element(By.ID, "newPage"))

value = "ASDASD"
driver.execute_script("arguments[0].setAttribute('value', '" + value +"')", driver.find_element(By.ID, "fname"))

