import json
from abc import ABC, abstractmethod
from pathlib import Path


class BaseSaver(ABC):
    """Абстрактынй класс для работы с файлами"""

    @abstractmethod
    def load_vacancy(self):
        """Абстрактный метод загрузки данных из JSON-файла."""
        pass

    @abstractmethod
    def _save_vacancy(self):
        """Абстрактный метод сохранения данных в файл."""
        pass

    @abstractmethod
    def add_vacancy(self):
        """Абстрактный метод добавления новых вакансий в файл и его сохранение"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Абстрактный метод для удаления вакансий из файла"""
        pass


class JSONSaver(BaseSaver):
    """Класс для работы с JSON файлом"""

    def __init__(self, path: str = r"../data/vacancies.json"):
        self.__path = Path(path)
        if not self.__path.exists():
            self._load_vacancy([])

    def load_vacancy(self):
        """Метод загрузки данных из JSON-файла."""
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

    def delete_vacancy(self, id_vacancies):
        """Абстрактный метод для удаления вакансий из файла"""

        data = self.load_vacancy()
        data_len_start = len(data)
        data = [vacancy for vacancy in data if vacancy.get("id") != id_vacancies]
        data_len_end = len(data)
        if data_len_start == data_len_end:
            print("Вакансия не найдена")
        else:
            print("Вакансия удалена")

        self._save_vacancy(data)
