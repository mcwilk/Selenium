from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Browser setup
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.implicitly_wait(1)
driver.maximize_window()
driver.get(r"http://www.kurs-selenium.pl/demo/")

# Set hotel or city
driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys("Dubai")
driver.find_element(By.XPATH, "//span[text()='Dubai']").click()

# Set check-in and check-out dates
# # 1st option
driver.find_element(By.NAME, "checkin").send_keys("12/03/2024")
driver.find_element(By.NAME, "checkout").send_keys("13/03/2024")

# # 2nd option
# driver.find_element(By.NAME, "checkin").click()
# driver.find_element(By.XPATH, "//td[@class='day ' and text()='26']").click()
# driver.find_element(By.NAME, "checkout").click()
# checkout_elems = driver.find_elements(By.XPATH, "//td[@class='day ' and text()='27']")
#
# for elem in checkout_elems:
#     if elem.is_displayed():
#         elem.click()
#         break

# Set travellers
driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.ID, "adultInput").clear()
driver.find_element(By.ID, "adultInput").send_keys("4")
driver.find_element(By.ID, "childInput").clear()
driver.find_element(By.ID, "childInput").send_keys("3")

# Search results
driver.find_element(By.XPATH, "//button[text()=' Search']").click()

# Get hotel names
hotels = driver.find_elements(By.XPATH, "//h4[contains(@class, 'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]

# Get hotel prices
prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]

for hotel, price in zip(hotel_names, price_values):
    print(f"Price for {hotel} is {price}.")

# Asserts
assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"

assert price_values[0] == "$22"
assert price_values[1] == "$50"
assert price_values[2] == "$80"
assert price_values[3] == "$150"

assert price_values == ["$22", "$50", "$80", "$150"]

driver.quit()
