import requests
from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Абстрактынй класс для работы с API"""

    @abstractmethod
    def connect(self):
        """Метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Метод получения вакансий по ключевому слову"""
        pass

class HeadHunterAPI(BaseApi):
    """Класс для работы с вакансиями через API Head Hunter """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"


    def connect(self):
        """Метод подключения к API"""

        response = requests.get(self.__url)
        if response.status_code != 200:
            print('Ошибка при обращении к API:', response.status_code)
        else:
            return response


    def get_vacancies(self, keyword, per_page = 20):
        """Метод получения вакансий по ключевому слову"""

        self.connect()
        params = {"text": keyword, "per_page": per_page}
        response = requests.get(self.__url, params=params)
        if response.status_code != 200:
            print('Ошибка при обращении к API:', response.status_code)
        else:
            return response.json().get("items", [])


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("Python", 10)
    print(vacancies)
