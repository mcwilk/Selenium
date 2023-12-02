from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# Detaches browser from the execution (it is not closed at the end)
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get("http://www.google.com")
driver.maximize_window()
