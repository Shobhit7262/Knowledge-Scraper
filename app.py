import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s",
                    datefmt="%d-%m-%Y  %H%:%M:%S",
                    level=logging.DEBUG,
                    filename="logs.txt")

logger =  logging.getLogger("scraping")

logger.info("Loading book list....")
page_content = requests.get("http://books.toscrape.com").content
page = AllBooksPage(page_content)

books = page.books


for i in range(1,page.page_limit):
    url = f"http://books.toscrape.com/catalogue/page-{i+1}.html"
    page_content = requests.get(url).content

    page = AllBooksPage(page_content)

    books.extend(page.books)

