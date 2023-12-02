import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\FileUpload.html")
driver.maximize_window()

upload_input = driver.find_element(By.ID, "myFile")
path = os.path.abspath(r"Files/uploadMe.txt")

driver.save_screenshot("Screenshots/before.png")
upload_input.send_keys(path)
driver.save_screenshot("Screenshots/after.png")
