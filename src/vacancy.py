

class Vacancy:
    __slots__ = ("name", "alternate_url", 'salary', 'salary_from', 'salary_to', "name_area")

    def __init__(self, name, alternate_url, salary, salary_from, salary_to, name_area):
        self.name = name
        self.alternate_url = alternate_url
        self.salary = self.__validate_salary(salary)
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.name_area = name_area or 'Регион не указан'

        self.__validate()

    def __validate(self) -> None:
        """Метод валидации данных вакансии"""

        if not self.name or not self.alternate_url:
            raise ValueError("Должны быть указаны имя и url адрес")
        if self.salary_from < 0 or self.salary_to < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        if self.salary_from is None and self.salary_to is None:
            if self.salary_from > self.salary_to:
                raise ValueError("Минимальная зарплата не может быть больше максимальной.")

    def __validate_salary(self, salary):
        """Метод для валидации суммы заработной платы"""

        if not isinstance(salary, (int, float)) or salary < 0:
            return 0
        return salary


    def __str__(self) -> str:
        """Метод строкового отображения вакансии"""
        return f'Вакансия: {self.name}, зарплата: от {self.salary_from} до {self.salary_to}, URL-адрес: {self.alternate_url}, регион: {self.name_area}'

    def __lt__(self, other: "Vacancy") -> bool:
        """Метод, сравнивающий вакансии по минимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 < (other.salary_from + other.salary_to) / 2

    def __gt__(self, other: "Vacancy") -> bool:
        """Метод, сравнивающий вакансии по максимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 > (other.salary_from + other.salary_to) / 2

    @staticmethod
    def cast_to_object_list(vacancies):
        """Метод для преобразования данных о вакансиях из JSON объекта в список объектов класса"""

        list_vacancies = []
        for vacancy in vacancies:
            name = vacancy.get("name", "Название вакансии не указано")
            url = vacancy.get("alternate_url")
            salary = vacancy.get("salary")
            salary_from = vacancy.get("salary", {}).get("from", 0) if vacancy.get("salary") else 0
            salary_to = vacancy.get("salary", {}).get("to", 0) if vacancy.get("salary") else 0

            area = vacancy.get("area")
            name_area = area.get("name", "Регион не указан") if area else "Описание не указано"

            vacancy = Vacancy(name=name, alternate_url=url, salary=salary, salary_from=salary_from, salary_to=salary_to,
                              name_area=name_area)

            list_vacancies.append(vacancy)

        return list_vacancies

    def to_dict(self):
        """Метод, преобразующий объект класса в словарь"""
        return {
            "name": self.name,
            "url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.name_area,
        }