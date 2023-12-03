from selenium.webdriver import Keys

from SecondAppTesting.POP.locators import locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        # locators
        self.username_input = locators.MyAccountLocators.username_id
        self.password_input = locators.MyAccountLocators.password_id
        self.login_button = locators.MyAccountLocators.login_name
        self.reg_email_input = locators.MyAccountLocators.reg_email_id
        self.reg_password_input = locators.MyAccountLocators.reg_password_id
        self.logout_link = locators.MyAccountLocators.logout_link_text
        self.error_msg = locators.MyAccountLocators.error_msg_xpath

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text
