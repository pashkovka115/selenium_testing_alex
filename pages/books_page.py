from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilites.logger_project import LoggerProject


class BooksPage(Base):
    __url = 'https://www.bookvoed.ru/books?genre=2'
    __id_selected_book = 0

    # locators
    __button_close_popup_change_city = '//div[@id="cityDetect"]//div[@class="Ey"]'
    __button_highly_rated = '//label[@for="highlyRated"]/../../div[2]' # '//label[@for="highlyRated"]'
    __ratings_all_books = '//div[@class="Rh"]//span[@class="Vr"]'
    __ratings_first_book = '//div[@class="Rh"][1]//span[@class="Vr"]'
    __button_applay_filters = '//button[@type="submit"][contains(text(), "Применить фильтры")]'
    __cookies_link_access = '//div[@id="cookieNoticeUser"]//a[@class="Vyb"]'
    __author_filter = '//input[@id="contributor-text"]'
    __authors_all_books = '//div[@class="Rh"]//div[@class="ps"]'
    __authors_first_books = '//div[@class="Rh"][1]//div[@class="ps"]'

    __first_book = '//div[@class="Rh"][1]'
    __first_book_link_to_detail = '//div[@class="Rh"][1]//a[contains(@class, "yWb")]'





    def __init__(self, driver):
        super().__init__(driver)

    # Getters

    def __get_button_close_popup_change_city(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_close_popup_change_city)))
        except TimeoutException as e:
            print('Попап смены города не найден')
            return None

    def __get_button_highly_rated(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_highly_rated)))
        except TimeoutException as e:
            print('Переключатель высокого рейтинга не найден')
            return None

    def __get_ratings_first_book(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__ratings_first_book)))
        except TimeoutException as e:
            print('Переключатель высокого рейтинга не найден')
            return None

    def __get_ratings_all_books(self, seconds=10):
        try:
            self.driver.implicitly_wait(seconds)
            return self.driver.find_elements(By.XPATH, self.__ratings_all_books)
        finally:
            print('Получены все рейтинги книг')
            self.driver.implicitly_wait(0)


    def __get_button_applay_filters(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_applay_filters)))
        except TimeoutException as e:
            print('Кнопка применения фильтров получена')
            return None


    def __get_cookies_link_access(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__cookies_link_access)))
        except TimeoutException as e:
            print('Ссылка согласия с куками получена')
            return None


    def __get_author_filter(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__author_filter)))
        except TimeoutException as e:
            print('Input фильтр по автору получен')
            return None


    def __get_authors_all_books(self, seconds=10):
        try:
            self.driver.implicitly_wait(seconds)
            return self.driver.find_elements(By.XPATH, self.__authors_all_books)
        finally:
            print('Получены все рейтинги книг')
            self.driver.implicitly_wait(0)

    def __get_authors_first_books(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__authors_first_books)))
        except TimeoutException as e:
            print('Переключатель высокого рейтинга не найден')
            return None

    def __get_first_book_link_to_detail(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__first_book_link_to_detail)))
        except TimeoutException as e:
            print('Получена ссылка на детальную страницу первой книги')
            return None

    def get_id_selected_book(self):
        return self.__id_selected_book

    # Actions

    def __click_button_close_popup_change_city(self, seconds=10):
        el = self.__get_button_close_popup_change_city(seconds)
        if el:
            el.click()
            print('click close_popup_change_city')


    def __click_button_highly_rated(self):
        el = self.__get_button_highly_rated()
        a = ActionChains(self.driver)
        a.move_to_element(el)
        self.pause(2)
        el.click()
        print('click_button_highly_rated')


    def __check_all_ratings(self):
        first = self.__get_ratings_first_book()
        flag = True
        if first:
            # чтобы все товары успели прогрузится
            self.pause(1)
            els = self.__get_ratings_all_books()
            # Рейтинг на сайте выбирается от 8 и выше
            for el in els:
                if float(el.text) < 8:
                    print(el.text)
                    flag = False
        print('check_all_ratings')

        assert True == flag, 'Не все рейтинги выше либо равны "8"'
        print('Рейтинги выбраны корректно')


    def __check_all_authors_names(self):
        first = self.__get_authors_first_books()
        flag = True
        if first:
            # чтобы все товары успели прогрузится
            self.pause(1)
            els = self.__get_authors_all_books()

            for el in els:
                if not 'Пушкин' in el.text:
                    print(el.text)
                    flag = False
        print('check_all_authors_names')

        assert True == flag, 'Не все имена соответствуют выбранному имени'
        print('Все имена соответствуют выбранному имени')


    def __click_button_applay_filters(self):
        el = self.__get_button_applay_filters()
        a = ActionChains(self.driver)
        a.move_to_element(el)
        self.pause(2)
        el.click()

    def __click_cookies_link_access(self):
        el = self.__get_cookies_link_access()
        if el:
            el.click()
        self.pause(2)

    def __input_author_filter(self):
        el = self.__get_author_filter()
        a = ActionChains(self.driver)
        a.move_to_element(el).perform()
        el.send_keys('Пушкин')
        self.pause(2)

    def __click_first_book_link_to_detail(self):
        el = self.__get_first_book_link_to_detail()
        if el:
            try:
                href = str(el.get_attribute('href'))
                self.__id_selected_book = int(href.split('?')[1].split('=')[1])
                print('ID:', self.__id_selected_book)
                el.click()
            except:
                pass
        self.pause(2)


    # Methods

    def select_book(self):
        LoggerProject.add_start_step(method='select_book')
        # если начали с этой страницы
        if self.driver.current_url == 'data:,':
            self.driver.maximize_window()
            self.driver.get(self.__url)

        self.__click_button_close_popup_change_city()
        self.__click_cookies_link_access()

        self.__click_button_highly_rated()
        self.__click_button_applay_filters()
        self.pause(2)
        self.__check_all_ratings()

        self.__input_author_filter()
        self.__click_button_applay_filters()
        self.__check_all_authors_names()

        # todo: только чтобы увидеть результат в браузере
        self.pause(5)

        self.__click_first_book_link_to_detail()

        LoggerProject.add_end_step(url=self.driver.current_url, method='select_book')
        print(f'Перешли на страницу детального просмотра книги id={self.get_id_selected_book()}')

