import json
from abc import ABC, abstractmethod
import os
from pathlib import Path
from src.vacancy import Vacancy

class BaseSaver(ABC):
    """Абстрактынй класс для работы с файлами"""

    @abstractmethod
    def load_vacancy(self):
        pass

    @abstractmethod
    def _save_vacancy(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(BaseSaver):
    """Класс для работы с JSON файлом"""

    def __init__(self, path: str = r"../data/vacancies.json"):
        self.__path = Path(path)
        if not self.__path.exists():
            self._load_vacancy([])

    def load_vacancy(self):
        """Приватный метод загрузки данных из JSON-файла."""
        try:
            with open(self.__path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")  # Обработка всех ошибок
            return []  # Возвращаем пустой список

    def _save_vacancy(self, data_):
        """Приватный метод сохранения данных в JSON-файл."""
        try:
            with open(self.__path, "w", encoding="utf-8") as file:
                json.dump(data_, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

    def add_vacancy(self, vacancies):
        """Метод добавления новых вакансий в JSON файл и его сохранение"""
        data_ = self.load_vacancy()
        data_.append(vacancies)
        self._save_vacancy(data_)


    def get_vacancies(self):
        pass

    def delete_vacancy(self):
        pass