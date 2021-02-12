from selenium.webdriver.firefox.options import Options
from selenium import webdriver

def create_driver(headless=True):
    """
    Create a selenium driver with headless as default.
    
    parameters:
        - headless: Boolean, True or False
    """

    opts = Options()

    if headless:
        opts.headless = True

    driver = webdriver.Firefox(options=opts)

    return driver
