import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start_maximized")
    # options.add_experimental_option("detach", True)
    chrome_service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.implicitly_wait(1)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
