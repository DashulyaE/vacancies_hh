from src.head_hunter_api import HeadHunterAPI
from src.utils import sorted_vacancies, find_vacancies
from src.vacancy import Vacancy


def user_interaction():

    hh_api = HeadHunterAPI()

    keyword = input("Введите ключевое слово для запроса на hh.ru: ")
    top_n = input("Введите количество вакансий для вывода в топ N по зарплате: ")
    filter_words = input("Введите ключевое слово для фильтрации полученных вакансий: ")

    if top_n.isdigit() and top_n != "0":
        top_n = int(top_n)
        vacancies = hh_api.get_vacancies(keyword)
        vacancies_top = sorted_vacancies(vacancies, top_n)
        vacancies_filter = find_vacancies(vacancies_top, filter_words)

        # вывод объектов класса Вакансии
        if vacancies_filter != []:
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
        else:
            print("Вакансий с указанными критериями не найдено")
    else:
        print("Кол-во вакансий должно быть числом")


if __name__ == "__main__":

    user_interaction()
