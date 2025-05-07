import pytest

from src.vacancy import Vacancy


def test_vacancy(vacancy):
    assert vacancy.id == "120168453"
    assert vacancy.name == "Backend-разработчик"
    assert vacancy.alternate_url == "https://hh.ru/vacancy/120168453"
    assert vacancy.salary_from == 5000000
    assert vacancy.salary_to == 15000000
    assert vacancy.name_area == "Ташкент"
    assert vacancy.snippet == "описание"


def test_vacancy_http():
    with pytest.raises(ValueError):
        obj_vac = Vacancy("120168000", "Backend", "некорректная ссылка", "100000", "5000000", "Ташкент", "описание")
        obj_vac._validate_url()
        assert "Ссылка на вакансию должна быть строкой."


def test_vacancy_validate_name():
    with pytest.raises(ValueError):
        obj_vac = Vacancy("120168123", 123, "некорректная ссылка", "100000", "6000000", "Ташкент", "описание")
        obj_vac._validate_name()
        assert "Название вакансии должно быть строкой."


def test_magic(vacancy, vacancy2, vacancy3, vacancy4):
    assert vacancy > vacancy2
    assert vacancy >= vacancy2
    assert vacancy < vacancy3
    assert vacancy <= vacancy3
    assert vacancy3 == vacancy4

def test_vacancy_str_method(capsys, vacancy):
    """Тест метода __str__ класса Vacancy с использованием capsys."""
    print(vacancy)  # Выводим объект в stdout
    captured = capsys.readouterr()  # Перехватываем вывод
    expected_output = f"ID: 120168453, Вакансия: Backend-разработчик, зарплата: от 5000000 до 15000000, URL-адрес: https://hh.ru/vacancy/120168453, регион: Ташкент, описание: описание\n"
    assert captured.out == expected_output
