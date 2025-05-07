import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def vacancy():
    return Vacancy(
        "120168453", "Backend-разработчик", "https://hh.ru/vacancy/120168453", 5000000, 15000000, "Ташкент", "описание"
    )


@pytest.fixture()
def vacancy2():
    return Vacancy("120168000", "Backend", "https://hh.ru/vacancy/120168453", 100000, 6000000, "Ташкент", "описание")


@pytest.fixture()
def vacancy3():
    return Vacancy("120168000", "Backend", "https://hh.ru/vacancy/120168453", 10000000, 11000000, "Ташкент", "описание")


@pytest.fixture()
def vacancy4():
    return Vacancy("120168111", "Backend", "https://hh.ru/vacancy/120168453", 10000000, 11000000, "Ташкент", "описание")
