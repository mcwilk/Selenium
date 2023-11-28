import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:

    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        yield
        self.driver.quit()