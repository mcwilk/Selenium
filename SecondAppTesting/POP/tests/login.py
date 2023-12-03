import pytest

from SecondAppTesting.POP.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_login_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("autotester123@gmail.com", "autotester123")

        assert my_account_page.is_logout_link_displayed()

    def test_login_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("autotester123@gmail.com", "autotesterXYZ")
        msg = "ERROR: Incorrect username or password"

        assert msg in my_account_page.get_error_msg()
