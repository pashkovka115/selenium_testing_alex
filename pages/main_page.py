from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilites.logger_project import LoggerProject


class MainPage(Base):
    __url = 'https://www.bookvoed.ru/'

    # locators

    __menu_top = '//div[@class="clb"]'
    __link_books = '//div[@class="clb"]//a[contains(text(), "Книги")]'

    __button_change_city = '//input[@type="button"][@value="Изменить город"]'
    __input_city = '//input[@id="cityDetect-cityd_input-text"]'




    def __init__(self, driver):
        super().__init__(driver)

    # Getters

    def __get_link_books(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__link_books)))
        except TimeoutException as e:
            print('Меню "Книги" не найдено')
            return None

    def __get_button_change_city(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_change_city)))
        except TimeoutException as e:
            print('Кнопки смены города в попапе не найдено')
            return None

    def __get_input_city(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__input_city)))
        except TimeoutException as e:
            print('Инпут для ввода города не найден')
            return None



    # Actions

    def __click_link_books(self, seconds=10):
        self.__get_link_books(seconds).click()
        print('click link books')

    def __click_button_change_city(self, seconds=10):
        el = self.__get_button_change_city(seconds)
        if el:
            el.click()
            print('click popup button change city')
            return True
        else:
            print('popup window not found')
            return False

    def __input_city_send_keys(self, seconds=10):
        el = self.__get_input_city(seconds)
        if el:
            el.send_keys('Краснодар')
            self.pause(1)
            el.send_keys(Keys.RETURN)

            print('send keys Краснодар')
        else:
            print('Город указан не был')


    # Methods

    def go_to_category_books(self):
        LoggerProject.add_start_step(method='go_to_category_books')
        self.driver.maximize_window()
        self.driver.get(self.__url)

        if self.__click_button_change_city():
            self.__input_city_send_keys()
            self.pause(2)

        self.__click_link_books(10)

        LoggerProject.add_end_step(url=self.driver.current_url, method='go_to_category_books')
        print('Перешли в категорию "Книги"')

