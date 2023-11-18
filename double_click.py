from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\DoubleClick.html")
driver.maximize_window()

button = driver.find_element(By.ID, "bottom")
# webdriver.ActionChains(driver).double_click(button).perform()

webdriver.ActionChains(driver).context_click(button).perform()
