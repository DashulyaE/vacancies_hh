from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    hh_api = HeadHunterAPI()

    #while True:

    keyword = input("Введите ключевое слово для запроса на hh.ru: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевое слово для фильтрации полученных вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
    # choice = input("\nВыберите номер для получения информации:  ")
    vacancies = hh_api.get_vacancies(keyword)
    #print(vacancies)
    for vacancy in vacancies[0]:
        vacancy = Vacancy(vacancy.get('id'), vacancy.get('name'), vacancy.get('alternate_url'),vacancy.get('salary'),vacancy.get('area').get('name'),vacancy.get('snippet'))
        print(vacancy)


if __name__ == "__main__":

    user_interaction()