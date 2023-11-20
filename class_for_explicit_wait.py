from selenium.webdriver.common.by import By


class WaitForListSize:

    def __init__(self, locator, expected_size):
        self.locator = locator
        self.expected_size = expected_size

    def __call__(self, driver):
        return len(driver.find_elements(By.XPATH, self.locator)) == self.expected_size
