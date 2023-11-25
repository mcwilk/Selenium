from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"https://www.w3schools.com/")
driver.maximize_window()

driver.find_element(By.ID, "accept-choices").click()

tutorials_element = driver.find_element(By.ID, "navbtn_tutorials")
webdriver.ActionChains(driver).move_to_element(tutorials_element).perform()

# webdriver.ActionChains(driver).drag_and_drop(draggable, target).perform()

webdriver.ActionChains(driver).move_to_element(tutorials_element).click(tutorials_element).perform()
