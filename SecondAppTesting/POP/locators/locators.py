from selenium.webdriver.common.by import By


class MyAccountLocators:

    my_account_xpath = (By.XPATH, "//li[@id='menu-item-22']//a")
    username_id = (By.ID, "username")
    password_id = (By.ID, "password")
    login_name = (By.NAME, "login")
    reg_email_id = (By.ID, "reg_email")
    reg_password_id = (By.ID, "reg_password")
    logout_link_text = (By.LINK_TEXT, "Logout")
    error_msg_xpath = (By.XPATH, "//ul[@class='woocommerce-error']//li")


class BillingAddressLocators:

    addresses_link_text = (By.LINK_TEXT, "Addresses")
    edit_link_text = (By.LINK_TEXT, "Edit")
    first_name_id = (By.ID, "billing_first_name")
    last_name_id = (By.ID, "billing_last_name")
    country_id = (By.ID, "billing_country")
    address_1_id = (By.ID, "billing_address_1")
    post_code_id = (By.ID, "billing_postcode")
    city_id = (By.ID, "billing_city")
    phone_id = (By.ID, "billing_phone")
    save_address_button_xpath = (By.XPATH, "//button[@value='Save address']")
    message_xpath = (By.XPATH, "//div[@class='woocommerce-message']")
