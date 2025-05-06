import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def vacancy():
    return Vacancy('120168453', 'Backend-разработчик','https://hh.ru/vacancy/120168453','5000000','15000000', 'Ташкент','описание')