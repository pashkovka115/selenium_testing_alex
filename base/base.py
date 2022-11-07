from datetime import datetime
from os.path import abspath

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from utilites.logger_selenium import LoggerSelenium


class Base():

    def __init__(self, driver=None):
        self.driver = driver

    @classmethod
    def get_driver(cls):
        caps = DesiredCapabilities().CHROME
        # caps["pageLoadStrategy"] = "normal"  # complete
        caps["pageLoadStrategy"] = "eager"  #  interactive
        # caps["pageLoadStrategy"] = "none"

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications" : 2})
        # отключить запись в логи (останавливается работа скрипта если версии не последние: selenium, chrom, chrom-driver)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--disable-blink-features")
        options.add_argument('--disable-blink-features=AutomationControlled')

        path_chromdriver = abspath('../../resourses/drivers/chromedriver.exe')
        s = Service(path_chromdriver)
        driver = EventFiringWebDriver(webdriver.Chrome(service=s, options=options, desired_capabilities=caps), LoggerSelenium())
        # driver.set_page_load_timeout(5)

        return driver

    def get_current_url(self):
        url = self.driver.current_url
        print(f'Current url: {url}')
        return url

    def assert_url(self, url):
        assert self.driver.current_url == url, f'Url {url} NOT correctly'
        print(f'Url {url} correctly')

    def get_screenshot(self, path_to_dir: str):
        date_now = datetime.utcnow().strftime('%Y.%m.%d-%H.%M.%S')
        screenshot_name = '/screenshot_' + date_now + '_.png'
        path_to_dir = path_to_dir.rstrip('/')
        self.driver.save_screenshot(path_to_dir + screenshot_name)


    def pause(self, seconds):
        a = ActionChains(self.driver)
        a.pause(seconds).perform()

    # ==========================================================================
    # def is_clickable(self, xpath, seconds=10):
    #     """ ожидает пока элемент станет кликабельным и возвращает True, иначе False """
    #     try:
    #         WebDriverWait(self.driver, seconds).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    #         return True
    #     except TimeoutException as te:
    #         return False
    #
    # def is_staleness(self, xpath, seconds=10):
    #     """ ожидает пока элемент исчезнет и возвращает True, иначе False """
    #     try:
    #         WebDriverWait(self.driver, seconds).until(EC.staleness_of((By.XPATH, xpath)))
    #         return True
    #     except TimeoutException as te:
    #         return False
    #
    # def is_visibility_of(self, element, seconds=10):
    #     """ ожидает пока существующий элемент станет видимым и возвращает True, иначе False """
    #     try:
    #         WebDriverWait(self.driver, seconds).until(EC.visibility_of(element))
    #         return True
    #     except TimeoutException as te:
    #         return False

    # def is_visibility_of(self, xpath, seconds=10):
    #     """ ожидает пока существующий элемент станет видимым и возвращает True, иначе False """
    #     try:
    #         WebDriverWait(self.driver, seconds).until(EC.visibility_of((By.XPATH, xpath)))
    #         return True
    #     except TimeoutException as te:
    #         return False

    # def is_not_visibility_of(self, xpath, seconds=10):
    #     """ ожидает пока существующий элемент станет не видимым и возвращает True, иначе False """
    #     try:
    #         WebDriverWait(self.driver, seconds).until_not(EC.visibility_of((By.XPATH, xpath)))
    #         return True
    #     except TimeoutException as te:
    #         return False
    #
    # def is_visibility_of_element_located(self, xpath, seconds=10):
    #     """ ожидает пока элемент появится и станет видимым и возвращает True, иначе False """
    #     try:
    #         WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    #         return True
    #     except TimeoutException as te:
    #         return False
    #
    # def is_presence(self, xpath, seconds=3):
    #     """ существуют ли элементы на странице. возвращает True если есть хотябы один иначе False """
    #     try:
    #         self.driver.implicitly_wait(seconds)
    #         return len(self.driver.find_elements(By.XPATH, xpath)) > 0
    #     finally:
    #         self.driver.implicitly_wait(0)

    # def is_not_presence(self, xpath, seconds=3):
    #     """ не существуют ли элементы на странице. возвращает True если нет иначе False """
    #     try:
    #         self.driver.implicitly_wait(seconds)
    #         return len(self.driver.find_elements(By.XPATH, xpath)) == 0
    #     finally:
    #         self.driver.implicitly_wait(0)


    # def get_element(self, xpath, seconds=3):
    #     # return self.driver.find_element(By.XPATH, xpath)
    #
    #     try:
    #         self.driver.implicitly_wait(seconds)
    #         return self.driver.find_element(By.XPATH, xpath)
    #     finally:
    #         self.driver.implicitly_wait(0)
    #
    # def get_elements(self, xpath, seconds=3):
    #     try:
    #         self.driver.implicitly_wait(seconds)
    #         return self.driver.find_elements(By.XPATH, xpath)
    #     finally:
    #         self.driver.implicitly_wait(0)
