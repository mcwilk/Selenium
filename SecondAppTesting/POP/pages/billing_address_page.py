from selenium.webdriver.support.select import Select

from SecondAppTesting.POP.locators.locators import BillingAddressLocators


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        # locators
        self.first_name_input = BillingAddressLocators.first_name_id
        self.last_name_input = BillingAddressLocators.last_name_id
        self.addresses_link = BillingAddressLocators.addresses_link_text
        self.edit_link = BillingAddressLocators.edit_link_text
        self.country_select = BillingAddressLocators.country_id
        self.address_input = BillingAddressLocators.address_1_id
        self.post_code_input = BillingAddressLocators.post_code_id
        self.city_input = BillingAddressLocators.city_id
        self.phone_input = BillingAddressLocators.phone_id
        self.save_address_button = BillingAddressLocators.save_address_button_xpath
        self.msg_div = BillingAddressLocators.message_xpath

    def open_edit_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()

    def set_personal_data(self, f_name, l_name):
        self.driver.find_element(*self.first_name_input).send_keys(f_name)
        self.driver.find_element(*self.last_name_input).send_keys(l_name)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.address_input).send_keys(street)
        self.driver.find_element(*self.post_code_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    def save_address(self):
        self.driver.find_element(*self.save_address_button).click()

    def get_message_text(self):
        return self.driver.find_element(*self.msg_div).text
