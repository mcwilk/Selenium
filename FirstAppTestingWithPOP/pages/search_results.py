import logging

from selenium.webdriver.common.by import By

from FirstAppTestingWithPOP.locators.locators import SearchResultLocators


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, SearchResultLocators.hotel_names_xpath)
        hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Available hotels are:")

        for name in hotel_names:
            self.logger.info(name)

        return hotel_names

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, SearchResultLocators.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Hotel prices are:")

        for price in hotel_prices:
            self.logger.info(price)

        return hotel_prices
