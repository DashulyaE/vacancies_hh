import requests
from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Абстрактынй класс для работы с API"""

    @abstractmethod
    def _connect(self):
        """Абстрактыный метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Абстрактыный метод получения вакансий по ключевому слову"""
        pass


class HeadHunterAPI(BaseApi):
    """Класс для работы с вакансиями через API Head Hunter"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "", "per_page": 100}
        self.__vacancies = []

    def _connect(self, keyword: str, per_page: int):
        """Метод подключения к API"""

        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        try:
            response = requests.get(self.__url, params=self.__params)
            if response.status_code == 200:
                return response
            else:
                raise Exception(f"Ошибка при обращении к API:, {response.status_code}")
        except Exception as e:
            print(f"Возникла ошибка при обращении к API , {e}")

    def get_vacancies(self, keyword: str, per_page: int = 100):
        """Метод получения вакансий по ключевому слову"""

        vacancies_list = []
        response = self._connect(keyword, per_page)
        if response:
            vacancies = response.json().get("items", [])
            vacancies_list.append(vacancies)
            if vacancies_list == [[]]:
                print("Вакансии не найдены")
        return vacancies_list
