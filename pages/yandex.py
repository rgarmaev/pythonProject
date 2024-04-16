#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='header-search')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//h3[@data-auto="snippet-title"]')

    # Button to sort products by price
    sort_products_by_price = WebElement(xpath='//button[@data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//span[@class="_3gYEe"]/following-sibling::span[@class="_1ArMm"]')
