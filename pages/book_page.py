from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilites.logger_project import LoggerProject


class BookPage(Base):
    __url = 'https://www.bookvoed.ru/book?id=6635665'
    __info_book = {}

    # locators

    __book_name = '//h1//span[@itemprop="name"]'
    __book_author = '//h1//span[@class="CD"]//a'
    __book_rating = '//div[@class="Ur"]//span[@class="Vr"]'
    __book_price = '//div[@id="book_buttons"]//div[@class="qD"]'
    __button_to_buy = '//div[@id="book_buttons"]//div[@itemprop="offers"]//a'
    __popup_button_to_cart = '//div[@id="bottom_action-bac"]//a[contains(text(), "Перейти в корзину")]'




    def __init__(self, driver, id_book):
        super().__init__(driver)
        self.id_book = id_book

    # Getters

    def __get_book_name(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__book_name)))
        except TimeoutException as e:
            print('Имя книги не найдено')
            return None

    def __get_book_author(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__book_author)))
        except TimeoutException as e:
            print('Автор книги не найден')
            return None

    def __get_book_rating(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__book_rating)))
        except TimeoutException as e:
            print('Рейтинг книги не найден')
            return None

    def __get_book_price(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__book_price)))
        except TimeoutException as e:
            print('Цена книги не найдена')
            return None

    def __get_button_to_buy(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_to_buy)))
        except TimeoutException as e:
            print('Ссылка на покупку книги не найдена')
            return None

    def __get_popup_button_to_cart(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__popup_button_to_cart)))
        except TimeoutException as e:
            print('Кнопка в попапе для перехода в корзину не найдена')
            return None


    def get_info_book(self):
        return self.__info_book


    # Actions

    def __collect_information_about_book(self, seconds=10):
        self.__info_book = {
            'id': self.id_book,
            'author': self.__get_book_author(seconds).text,
            'name': self.__get_book_name(seconds).text,
            'rating': self.__get_book_rating(seconds).text,
            'price': self.__get_book_price(seconds).text
        }

        print('Получена информация о книге')


    def __click_button_to_buy(self):
        self.__get_button_to_buy().click()


    def __click_popup_button_to_cart(self):
        self.__get_popup_button_to_cart().click()


    # Methods

    def move_to_cart(self):
        print(f'Current URL:', self.driver.current_url)
        print(f'property URL:', self.__url)

        LoggerProject.add_start_step(method='move_to_cart')
        # если начали с этой страницы
        if self.driver.current_url == 'data:,':
            self.driver.maximize_window()
            self.driver.get(self.__url)

        self.__collect_information_about_book()
        self.__click_button_to_buy()
        self.pause(2)
        self.__click_popup_button_to_cart()


        LoggerProject.add_end_step(url=self.driver.current_url, method='move_to_cart')
        print('Перешли в корзину')

