def sorted_vacancies(vacancies, count):
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


def find_vacancies(vacancies, keyword):
    """Возвращает список вакансий, содержащих ключевое слово."""
    result = []
    result = [
        vacancy for vacancy in vacancies if any(keyword.lower() in str(value).lower() for value in vacancy.values())
    ]
    return result
