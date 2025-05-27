import os


from config import DATA_DIR
from src.filehandler import JSONSaver


def test_save_load():
    name_file = "test_data.json"
    operations_path = os.path.join(DATA_DIR, name_file)
    json_obj = JSONSaver(operations_path)
    data_to_save = [
        {"id": "120288679", "name": "Программист-разработчик", "alternate_url": "https://hh.ru/vacancy/120288679"},
        {"id": "120288777", "name": "Программист", "alternate_url": "https://hh.ru/vacancy/120288777"},
    ]
    assert json_obj._save_vacancy(data_to_save) is None
    loaded_data = json_obj.load_vacancy()
    assert loaded_data == data_to_save


def test_add_vacancy():
    name_file = "test_data.json"
    operations_path = os.path.join(DATA_DIR, name_file)
    json_obj = JSONSaver(operations_path)
    json_obj.delete_vacancy("120288427")
    assert "Вакансия не найдена"
    json_obj.delete_vacancy("120288679")
    assert "Вакансия удалена"
