import logging

from selenium.webdriver.common.by import By

from FirstAppTestingWithPOP.locators.locators import SearchHotelLocators


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def set_city(self, city):
        self.logger.info(f"Setting city {city}")
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, SearchHotelLocators.location_match_span_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info(f"Setting check in {check_in} and check out {check_out} dates")
        self.driver.find_element(By.NAME, SearchHotelLocators.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, SearchHotelLocators.check_out_input_name).send_keys(check_out)

    def set_travellers(self, adults, children):
        self.logger.info(f"Setting travellers: {adults} adults and {children} children")
        self.driver.find_element(By.ID, SearchHotelLocators.travellers_input_id).click()
        self.driver.find_element(By.ID, SearchHotelLocators.adult_input_id).clear()
        self.driver.find_element(By.ID, SearchHotelLocators.adult_input_id).send_keys(adults)
        self.driver.find_element(By.ID, SearchHotelLocators.child_input_id).clear()
        self.driver.find_element(By.ID, SearchHotelLocators.child_input_id).send_keys(children)

    def perform_search(self):
        self.logger.info("Performing search...")
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_button_xpath).click()
