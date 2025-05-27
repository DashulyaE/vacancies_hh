class Vacancy:
    """Класс для работы с вакансией"""

    __slots__ = ("id", "name", "alternate_url", "salary_from", "salary_to", "name_area", "snippet")

    def __init__(
        self,
        id: str,
        name: str,
        alternate_url: str,
        salary_from: float,
        salary_to: float,
        name_area: str,
        snippet: str,
    ):
        self.id = id
        self.name = self._validate_name(name)
        self.alternate_url = self._validate_url(alternate_url)
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else salary_from
        self.name_area = name_area or "Регион не указан"
        self.snippet = snippet or "Описания нет"

    def _validate_name(self, name: str):
        """Проверяет, что название вакансии является строкой."""
        if not isinstance(name, str):
            raise ValueError("Название вакансии должно быть строкой.")
        return name

    def _validate_url(self, alternate_url: str):
        """Проверяет, что ссылка на вакансию является
        строкой и начинается с "http"."""
        if not isinstance(alternate_url, str) or not alternate_url.startswith("http"):
            raise ValueError("Ссылка на вакансию должна быть строкой.")
        return alternate_url

    def __lt__(self, other: "Vacancy"):
        """Метод, сравнивающий вакансии по минимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 < (other.salary_from + other.salary_to) / 2

    def __gt__(self, other: "Vacancy"):
        """Метод, сравнивающий вакансии по максимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 > (other.salary_from + other.salary_to) / 2

    def __eq__(self, other: "Vacancy"):
        """Магический метод, возвращающий True, если зарплата
        текущей вакансии равна зарплате другой вакансии."""
        return (self.salary_from + self.salary_to) / 2 == (other.salary_from + other.salary_to) / 2

    def __le__(self, other: "Vacancy"):
        """Магический метод, возвращающий True, если зарплата
        текущей вакансии меньше или равна зарплате другой вакансии."""
        return (self.salary_from + self.salary_to) / 2 <= (other.salary_from + other.salary_to) / 2

    def __ge__(self, other: "Vacancy"):
        """Магический метод, возвращающий True, если зарплата
        текущей вакансии больше или равна зарплате другой вакансии."""
        return (self.salary_from + self.salary_to) / 2 >= (other.salary_from + other.salary_to) / 2

    def __str__(self):
        """Метод строкового отображения вакансии"""
        return (
            f"ID: {self.id}, Вакансия: {self.name}, зарплата: от {self.salary_from} до {self.salary_to}, "
            f"URL-адрес: {self.alternate_url}, регион: {self.name_area}, описание: {self.snippet}"
        )

    def to_dict(self):
        """Метод, преобразующий объект класса в словарь"""
        return {
            "id": self.id,
            "name": self.name,
            "url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "name_area": self.name_area,
            "snippet": self.snippet,
        }
