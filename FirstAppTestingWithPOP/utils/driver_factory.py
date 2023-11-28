from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_experimental_option("detach", True)
            chrome_service = webdriver.ChromeService(ChromeDriverManager().install())

            return webdriver.Chrome(service=chrome_service, options=options)

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("start-maximized")
            options.add_experimental_option("detach", True)
            edge_service = webdriver.EdgeService(EdgeChromiumDriverManager().install())

            return webdriver.Edge(service=edge_service, options=options)

        raise Exception("Provide valid browser name!")
