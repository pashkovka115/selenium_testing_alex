import sys
import time
from os.path import abspath

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.book_page import BookPage
from pages.cart_page import CartPage

sys.path.append("../")

from pages.books_page import BooksPage
from base.base import Base
from pages.main_page import MainPage


def test_buy_product():
    driver = Base().get_driver()
    # driver.find_element(By.XPATH, '//body').send_keys(Keys.F12)

    try:
        mp = MainPage(driver)
        mp.go_to_category_books()

        booksp = BooksPage(driver)
        booksp.select_book()

        # bookp = BookPage(driver, '6635665')
        bookp = BookPage(driver, booksp.get_id_selected_book())
        bookp.move_to_cart()

        cp = CartPage(driver, bookp.get_info_book())
        cp.go_to_checkout()


    # except TimeoutException as e:
    #     pass
    #     driver.execute_script('window.stop();')

    except Exception as e:
        print(e)

    finally:
        time.sleep(4)
        driver.quit()
