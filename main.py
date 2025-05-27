import os

from config import DATA_DIR
from src.filehandler import JSONSaver
from src.head_hunter_api import HeadHunterAPI
from src.utils import sorted_vacancies, find_vacancies, vacancies_to_obj


def user_interaction(): # pragma: no cover

    hh_api = HeadHunterAPI()
    name_file = "vacancies.json"
    operations_path = os.path.join(DATA_DIR, name_file)
    json_obj = JSONSaver(operations_path)
    keyword = input("Введите ключевое слово для запроса на hh.ru: ")
    top_n = input("Введите количество вакансий для вывода в топ N по зарплате: ")
    filter_words = input("Введите ключевое слово для фильтрации полученных вакансий: ")

    if top_n.isdigit() and top_n != "0":
        top_n = int(top_n)
        vacancies = hh_api.get_vacancies(keyword)
        vacancies_top = sorted_vacancies(vacancies, top_n)
        vacancies_filter = find_vacancies(vacancies_top, filter_words)
        vacancies_load = json_obj.load_vacancy()
        for vacancy_filter in vacancies_filter:
            if vacancy_filter not in vacancies_load:
                json_obj.add_vacancy(vacancy_filter)

        # вывод объектов класса Вакансии
        if vacancies_filter != []:
            vacancies_to_obj(vacancies_filter)
        else:
            print("Вакансий с указанными критериями не найдено")
    else:
        print("Кол-во вакансий должно быть числом")
    print("Прочитать содержимое файла с сохраненными вакансиями?")
    answer_1 = str(input("Ответ (да/нет): ")).title()
    if answer_1 in ["Да", "Yes"]:
        read_file = json_obj.load_vacancy()
        vacancies_to_obj(read_file)
        print("Удалить вакансию по ID записи?")
        answer_2 = str(input("Ответ (да/нет): ")).title()
        if answer_2 in ["Да", "Yes"]:
            print("Введите ID записи:")
            answer_3 = str(input("Ответ: ")).title()
            json_obj.delete_vacancy(answer_3)
        else:
            print("Работа программы завершена")
    else:
        print("Работа программы завершена")


if __name__ == "__main__": # pragma: no cover

    user_interaction()