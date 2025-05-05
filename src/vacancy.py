

class Vacancy:
    """Класс для работы с вакансией"""

    __slots__ = ("id", "name", "alternate_url", 'salary', "name_area", "snippet")

    def __init__(self, id, name, alternate_url, salary, name_area, snippet):
        self.id = id
        self.name = self.__validate_name(name)
        self.alternate_url = self.__validate_url(alternate_url)
        self.salary = self.__validate_salary(salary)
        self.name_area = name_area
        self.snippet = snippet or 'Описание вакансии не указано'

    def __validate_name(self,name):
        """Метод валидации названия вакансии"""

        if not isinstance(name, str) or not name:
            return "Название вакансии не указано"
        return name

    def __validate_url(self, alternate_url):
        """Метод валидации ссылки на вакансию """

        if not isinstance(alternate_url, str) or not alternate_url.startswith("http"):
            return "Cсылка на вакансию должна быть строкой и начинаться с http"
        return alternate_url

    def __validate_salary(self, salary):
        """Метод валидации зарплаты"""

        if not isinstance(salary, (int, float)) or salary < 0:
            return 0
        return salary

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary != other.salary

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary

    def __str__(self) -> str:
        """Метод строкового отображения вакансии"""
        return (f'ID: {self.id}, Вакансия: {self.name}, зарплата: {self.salary}, '
                f'URL-адрес: {self.alternate_url}, регион: {self.name_area}, описание: {self.snippet}')


    def to_dict(self):
        """Метод, преобразующий объект класса в словарь"""
        return {
            "id": self.id,
            "name": self.name,
            "url": self.alternate_url,
            "salary": self.salary,
            "description": self.name_area,
            "snippet": self.snippet
        }



