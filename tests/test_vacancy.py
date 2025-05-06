

def test_vacancy(vacancy):
    assert vacancy.id == '120168453'
    assert vacancy.name == 'Backend-разработчик'
    assert vacancy.alternate_url == 'https://hh.ru/vacancy/120168453'
    assert vacancy.salary_from == '5000000'
    assert vacancy.salary_to == '15000000'
    assert vacancy.name_area == 'Ташкент'
    assert vacancy.snippet == 'описание'
