from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# Detaches browser from the execution (it is not closed at the end)
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(r"C:\Users\mwilk\PycharmProjects\Selenium\Files\Test.html")
driver.maximize_window()

# ACTIONS ON ELEMENTS
driver.find_element(by=By.ID, value="clickOnMe").click()
driver.switch_to.alert.accept()
button = driver.find_element(by=By.ID, value="clickOnMe")
button.click()
driver.switch_to.alert.dismiss()
# driver.find_element(by=By.TAG_NAME, value="p").click()
driver.find_element(By.ID, "fname").send_keys("ABCDEFGH")
# driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
auto_select = Select(driver.find_element(By.TAG_NAME, "select"))
auto_select.select_by_visible_text("Volvo")
auto_select.select_by_value("saab")
auto_select.select_by_index(3)
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//input[@value='female']").click()
print(driver.find_element(By.TAG_NAME, "h1").text)
print(driver.find_element(By.ID, "clickOnMe").text)
print(driver.find_element(By.CLASS_NAME, "topSecret").get_attribute("textContent"))
print(driver.find_element(By.ID, "fname").get_attribute("value"))
# print(driver.find_element(By.ID, "smileImage").size.get("height"))
print(driver.find_element(By.ID, "smileImage").get_attribute("naturalHeight"))
assert driver.find_element(By.ID, "smileImage").get_attribute("naturalHeight") != '0'

print(driver.title)
current_window_name = driver.current_window_handle
driver.find_element(By.ID, "newPage").click()
all_window_names = driver.window_handles
print(all_window_names)

for window in all_window_names:
    if window != current_window_name:
        driver.switch_to.window(window)

print(driver.title)
driver.switch_to.window(current_window_name)
print(driver.title)

# driver.quit()
