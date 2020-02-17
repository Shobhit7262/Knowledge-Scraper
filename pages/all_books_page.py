import re
from bs4 import BeautifulSoup

from locators.all_books_page_locator import AllBooksPageLocator
from parser.book_parser import BookParser



class AllBooksPage:
    def __init__(self , page_content):
        self.soup = BeautifulSoup(page_content , "html.parser")

    @property
    def books(self):
        return  [BookParser(e) for e in self.soup.select(AllBooksPageLocator.BOOKS)]

    @property
    def page_limit(self):
        content = self.soup.select_one(AllBooksPageLocator.PAGER).string

        pattern = "[A-Za-z ]+[0-9 ]+[A-Za-z ]+([0-9]+)"

        matches = re.search(pattern , content)
        got = int(matches.group(1))
        return got

