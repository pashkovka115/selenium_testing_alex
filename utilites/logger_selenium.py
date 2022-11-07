from datetime import datetime
from os.path import abspath

from selenium.webdriver.support.events import AbstractEventListener


class LoggerSelenium(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print(f"\nНачальный адрес {url}")

    # def after_navigate_to(self, url, driver):
    #     print(f"After navigate to {url}")

    def before_find(self, by, value, driver):
        print(by, value, '"поиск элемента..."')

    def after_find(self, by, value, driver):
        print(by, value, '"элемент найден"')

    def on_exception(self, exception, driver):
        exception = str(exception)
        exception = exception[: exception.find('Stacktrace:')]

        print('\n\n', exception, f'[ ERROR ] элемент НЕ найден на странице {driver.current_url}')
        for line in driver.get_log("browser"):
            print('log from browser ===', line)

        date_now = datetime.utcnow().strftime('%Y.%m.%d-%H.%M.%S')
        screenshot_name = '/ERROR_screenshot_' + date_now + '_.png'
        driver.save_screenshot(abspath('../screens') + screenshot_name)

        driver.quit()
