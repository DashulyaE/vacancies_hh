from src.head_hunter_api import HeadHunterAPI
from src.utils import filter_vacancies
from src.vacancy import Vacancy


def user_interaction():
    hh_api = HeadHunterAPI()

    #while True:

    keyword = input("Введите ключевое слово для запроса на hh.ru: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N по зарплате: "))
    # filter_words = input("Введите ключевое слово для фильтрации полученных вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
    # choice = input("\nВыберите номер для получения информации:  ")
    vacancies = hh_api.get_vacancies(keyword)
    #vacancies_filter = filter_vacancies(vacancies, top_n)
    #print(vacancies)

    #вывод объектов класса Вакансии
    for vacancy in vacancies[0]:
        salary_from = vacancy.get("salary", {}).get("from", 0) if vacancy.get(
            "salary") else 0
        # Если есть salary, Обращаемся к вакансии по ключу salary, внутри обращаемся по ключу "from"
        salary_to = vacancy.get("salary", {}).get("to", 0) if vacancy.get("salary") else 0

        vacancy = Vacancy(vacancy.get('id'), vacancy.get('name'), vacancy.get('alternate_url'), salary_from, salary_to, vacancy.get('area').get('name'), vacancy.get('snippet'))
        print(vacancy)


if __name__ == "__main__":

    user_interaction()