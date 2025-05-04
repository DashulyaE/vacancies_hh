import requests
from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Абстрактынй класс для работы с API"""

    @abstractmethod
    def _connect(self):
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


    def _connect(self):
        """Метод подключения к API"""

        response = requests.get(self.__url)
        if response.status_code != 200:
            print('Ошибка при обращении к API:', response.status_code)
        else:
            return response


    def get_vacancies(self, keyword, per_page = 20):
        """Метод получения вакансий по ключевому слову"""

        self._connect()
        params = {"text": keyword, "per_page": per_page}
        response = requests.get(self.__url, params=params)
        if response.status_code != 200:
            print('Ошибка при обращении к API:', response.status_code)
        else:
            vacancies = response.json().get("items", [])
            return [
                {
                    'name': vacancy['name'],
                    'area': vacancy['area']['name'],
                    'url': vacancy['alternate_url'],
                    'salary': vacancy.get('salary'),
                    'id': vacancy.get('id')
                }
                for vacancy in vacancies
            ]

