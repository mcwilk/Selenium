from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("http://www.google.com")
