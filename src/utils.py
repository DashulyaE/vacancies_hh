from typing import List

from src.vacancy import Vacancy


def sorted_vacancies(vacancies: List[dict], count: int):
    """Функция сортирует и выдает топ вакансий по размеру зарплаты"""
    sorted_vacancies = sorted(
        vacancies[0],
        key=lambda v: (
            (v.get("salary", {}).get("to") or v.get("salary", {}).get("from") or 0)
            if isinstance(v.get("salary"), dict)
            else 0
        ),
        reverse=True,
    )
    top_vacancies = sorted_vacancies[:count]
    return top_vacancies


def find_vacancies(vacancies: List[dict], keyword: str):
    """Возвращает список вакансий, содержащих ключевое слово."""
    result = []
    result = [
        vacancy for vacancy in vacancies if any(keyword.lower() in str(value).lower() for value in vacancy.values())
    ]
    return result


def vacancies_to_obj(vacancies_filter: List[dict]):
    for vacancy in vacancies_filter:
        salary_from = vacancy.get("salary", {}).get("from", 0) if vacancy.get("salary") else 0
        salary_to = vacancy.get("salary", {}).get("to", 0) if vacancy.get("salary") else 0
        vacancy = Vacancy(
            vacancy.get("id"),
            vacancy.get("name"),
            vacancy.get("alternate_url"),
            salary_from,
            salary_to,
            vacancy.get("area").get("name"),
            vacancy.get("snippet"),
        )
        print(vacancy)
