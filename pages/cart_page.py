import random
import re

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilites.logger_project import LoggerProject


class CartPage(Base):
    __url = ''
    __info_book = {}

    # locators

    __book_name = '//div[@id="order2-cart"]//h5//a'
    __book_author = '//div[@id="order2-cart"]//h5[2]'
    __book_price = '//div[@id="order2-cart"]//span[@class="Zh"]//span[contains(@class, "Yh")]'

    __button_checkout = '//a[contains(text(), "Перейти к оформлению")]'

    __input_user_name = '//div[contains(@class, "Mbb")]//input[@name="name"]'
    __input_email = '//div[contains(@class, "Mbb")]//input[@id="order2-email-input"]'
    # вводить номер после +7. "mask":"+7 000 000 00 00"
    __input_phone = '//div[contains(@class, "Mbb")]//input[@id="order2-phone-input"]'

    # todo
    __delivery_courier = '//div[@id="order2-orderDeliveryTiles"]//input[@value="441"]//parent::label'

    __delivery_street = '//input[@id="order2-street-text"]'
    __delivery_house = '//*[@id="order2"]//input[@name="house"]'
    __delivery_aportment = '//*[@id="order2"]//input[@name="flat"]'
    __delivery_address_comment = '//*[@id="order2"]//input[@name="addressComment"]'
    __payment_method = '//*[@id="order2-orderPaymentTiles"]/div/div/div[1]/label'

    __checkbox_accept = '//*[@id="order2"]//input[@name="accept"]'
    __button_order = '//*[@id="order2"]//a[@class][contains(text(), "Заказать")]'

    # todo: заполнить форму отправки заказа в корзине




    def __init__(self, driver, info_book):
        super().__init__(driver)
        self.__info_book = info_book

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

    def __get_book_price(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__book_price)))
        except TimeoutException as e:
            print('Цена книги не найдена')
            return None

    def __get_button_checkout(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_checkout)))
        except TimeoutException as e:
            print('Цена книги не найдена')
            return None

    def __get_input_user_name(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__input_user_name)))
        except TimeoutException as e:
            print('Поле ввода имени пользователя не найдено')
            return None

    def __get_input_email(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__input_email)))
        except TimeoutException as e:
            print('Поле ввода email не найдено')
            return None

    def __get_input_phone(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__input_phone)))
        except TimeoutException as e:
            print('Поле ввода телефона не найдено')
            return None

    def __get_delivery_courier_button(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__delivery_courier)))
        except TimeoutException as e:
            print('Поле выбора способа доставки не найдено')
            return None

    def __get_delivery_street(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__delivery_street)))
        except TimeoutException as e:
            print('Поле ввода улицы доставки не найдено')
            return None

    def __get_delivery_house(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__delivery_house)))
        except TimeoutException as e:
            print('Поле ввода номера дома доставки не найдено')
            return None

    def __get_delivery_aportment(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__delivery_aportment)))
        except TimeoutException as e:
            print('Поле ввода номера квартиры доставки не найдено')
            return None

    def __get_delivery_address_comment(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__delivery_address_comment)))
        except TimeoutException as e:
            print('Поле ввода Примечание к адресу не найдено')
            return None

    def __get_payment_method(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__payment_method)))
        except TimeoutException as e:
            print('Поле способа оплаты не найдено')
            return None

    def __get_checkbox_accept(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__checkbox_accept)))
        except TimeoutException as e:
            print('Чекбокс согласия с совершеннолетием не найден')
            return None

    def __get_button_order(self, seconds=10):
        try:
            return WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_order)))
        except TimeoutException as e:
            print('Итоговая кнопка заказа не найдена')
            return None


    # Actions

    def __check_book_data(self, seconds=10):
        print('=== START ASSERT BOOK FROM CART ===')

        assert self.__info_book['name'] == self.__get_book_name(seconds).text, 'Название книги не совпадает'
        print('Название книги совпадает')
        assert self.__info_book['author'] == str(self.__get_book_author(seconds).text).replace(',', ''), 'Имя автора не совпадает'
        print('Имя автора совпадает')

        s1 = self.__info_book['price']
        res1 = re.search(r"[\d\.]+", s1).group(0)

        s2 = self.__get_book_price(seconds).text
        res2 = re.search(r"[\d\.]+", s2).group(0)

        print('REGEXP:', res1, res2)
        assert res1 == res2, 'Цена не совпадает'
        print('Цена совпадает')

        print('=== END ASSERT BOOK ===')

    def __click_button_checkout(self):
        self.__get_button_checkout().click()


    def __input_form_user_info(self):
        self.__get_input_user_name().send_keys('Иванов Иван Иванович')
        self.__get_input_email().send_keys(f'pariss{random.randint(1, 100000)}@mail.ru')
        self.__get_input_phone().clear()
        self.__get_input_phone().send_keys(f'+7928{random.randint(1, 100000)}00{random.randint(1, 100000)}8{random.randint(1, 100000)}2')

        self.pause(3)

        self.__get_delivery_courier_button().click()
        self.pause(10)

        self.__get_delivery_street().send_keys('Красная')
        self.__get_delivery_house().send_keys('11')
        self.__get_delivery_aportment().send_keys('-')
        self.__get_delivery_address_comment().send_keys('Частный дом')

        self.pause(3)

        self.__get_payment_method().click()
        self.__get_checkbox_accept().click()

        self.pause(3)

        # todo: только чтобы увидеть результат
        self.pause(3)
        self.__get_button_order().click()


    # Methods

    def go_to_checkout(self):
        print('Корзина', f'Current URL:', self.driver.current_url)

        LoggerProject.add_start_step(method='move_to_cart')

        self.__check_book_data()
        self.__click_button_checkout()
        self.pause(1)
        self.__input_form_user_info()


        LoggerProject.add_end_step(url=self.driver.current_url, method='move_to_cart')
        print('Заказ оформлен. Перешли к оплате.')

