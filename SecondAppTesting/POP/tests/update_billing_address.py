import random

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from SecondAppTesting.POP.pages.billing_address_page import BillingAddressPage
from SecondAppTesting.POP.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        suffix = str(random.randint(1, 10000))
        my_account_page = MyAccountPage(self.driver)
        billing_address_page = BillingAddressPage(self.driver)

        my_account_page.open_page()
        my_account_page.create_account(f"autotester{suffix}@gmail.com", "autotester123")

        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("Andreas", "Doe")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Niepodleglosci 12", "10-121", "Cracow")
        billing_address_page.set_phone_number("111222333")
        billing_address_page.save_address()

        assert billing_address_page.get_message_text() == "Address changed successfully."
