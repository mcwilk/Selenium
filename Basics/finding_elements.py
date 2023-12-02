from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# Detaches browser from the execution (it is not closed at the end)
# options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Test.html")
driver.maximize_window()
driver.find_element(by=By.ID, value="clickOnMe")
driver.find_element(by=By.NAME, value="fname")
driver.find_element(by=By.LINK_TEXT, value="Visit W3Schools.com!")
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Visit W3Sc")
driver.find_element(by=By.CLASS_NAME, value="topSecret")
driver.find_element(by=By.TAG_NAME, value="a")
driver.find_element(by=By.TAG_NAME, value="p")
driver.find_element(by=By.CSS_SELECTOR, value="a")
driver.find_element(by=By.CSS_SELECTOR, value="img#smileImage")
driver.find_element(by=By.CSS_SELECTOR, value="p.topSecret")
print(driver.find_element(by=By.CSS_SELECTOR, value="th:first-child").tag_name)
print(driver.find_element(By.XPATH, "html/body/table/tbody/tr/th").text)
print(driver.find_element(By.XPATH, "//th").text)
print(driver.find_element(By.XPATH, "//th[text( )='Month']").text)
print(len(driver.find_elements(By.XPATH, "//th")))
# driver.quit()
