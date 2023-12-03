import random

import pytest

from SecondAppTesting.POP.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("autotester123@gmail.com", "autotester123")
        msg = "Error: An account is already registered"

        assert msg in my_account_page.get_error_msg()

    def test_create_account_passed(self):
        suffix = str(random.randint(1, 10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(f"autotester{suffix}@gmail.com", "autotester123")

        assert my_account_page.is_logout_link_displayed()
