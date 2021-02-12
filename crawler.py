from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.nasdaq.com/market-activity/stocks"
BASE_XPATH = "/html/body/div[2]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[1]/span[2]"

def open_stock_page(stock_symbol):
    try:
        opts = Options()
        opts.headless = True
        driver = webdriver.Firefox(options=opts)
        driver.get(f"{BASE_URL}/{stock_symbol}")
    except Exception as e:
        print("Error while loading driver")

    return driver


def get_stock_price(driver):
    try:
        stock_price = driver.find_element_by_xpath(BASE_XPATH)
    except Exception as e:
        print("Error while loading stock price")

    return stock_price.text


if __name__ == "__main__":
    stock_name = 'ipoe'
    stock_page = open_stock_page(stock_name)
    while True:
        price = get_stock_price(stock_page)
        print(f"Current Price for {stock_name}: {price}", end="\r")
        time.sleep(1)
        
