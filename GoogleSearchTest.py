from selenium import webdriver


chrome_service = webdriver.ChromeService(r".\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("http://www.google.com")
