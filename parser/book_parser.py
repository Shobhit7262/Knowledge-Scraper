import re
from bs4 import BeautifulSoup

from locators.books_locators import BooksLocators






class BookParser:

    RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    def __init__(self , parent):
        self.parent = parent

    def __repr__(self):
        return f"<The book {self.name} with price £{self.price} has {self.star_rating} star>"


    @property
    def name(self):
        locator = BooksLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs["title"]
        return item_name

    @property
    def link(self):
        locator = BooksLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs["href"]
        return item_link

    @property
    def price(self):
        locator = BooksLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = "£([0-9]+\.[0-9]+)"

        matches = re.search(pattern , item_price)
        return (float(matches.group(1)))

    @property
    def star_rating(self):
        locator = BooksLocators.RATING_LOCATOR
        rating = self.parent.select_one(locator).attrs["class"]
        rating_list = [r for r in rating if r != "star-rating"]
        rating_number = BookParser.RATINGS.get(rating_list[0])
        return rating_number










