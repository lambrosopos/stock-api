import os
import json
import datetime
from flask import Blueprint
from app.utils.selenium import create_driver

bp = Blueprint('stock_api', __name__, url_prefix='/api')

driver = create_driver()
current_symbol = ''

@bp.route('/')
def index():
    return 'OK', 200

def get_page(stock_symbol):
    API_URL = f"{os.getenv('STOCK_API_URL')}/{stock_symbol}"
    driver.get(API_URL)

@bp.route('/<stock_symbol>')
def get_info(stock_symbol=None):
    global current_symbol

    if not stock_symbol:
        return 'NEED SYMBOL'

    if current_symbol != stock_symbol:
        get_page(stock_symbol)
        current_symbol = stock_symbol

    API_SELECTOR = os.getenv('STOCK_API_CSS_SELECTOR')

    stock_price = driver.find_element_by_css_selector(API_SELECTOR)

    resp = {
        'stock_symbol':stock_symbol.upper(),
        'stock_price':stock_price.text[1:],
        'timestamp': datetime.datetime.now().__str__(),
        'currency':stock_price.text[0]
    }

    return resp, 200
