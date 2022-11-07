import datetime
import os
from os.path import abspath


class LoggerProject():
    file_name = abspath('../logs') + '/' + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def __write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as f:
            f.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"

        cls.__write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n===================\n"

        cls.__write_log_to_file(data_to_add)


    @classmethod
    def error(cls, method, data: str):
        sentence = '[!!! Error !!!] '
        sentence += f'Method: {method}. '
        sentence += data
        sentence += f"\n===================\n"
        exit()