from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    hh_api = HeadHunterAPI()

    while True:

        keyword = input("Введите ключевое слово для запроса на hh.ru: ")
        # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        # filter_words = input("Введите ключевое слово для фильтрации полученных вакансий: ").split()
        # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
        # choice = input("\nВыберите номер для получения информации:  ")
        vacancies = hh_api.get_vacancies(keyword)

        if vacancies:
            for vacancy in vacancies:
                print(
                    f"Название: {vacancy['name']}, Регион: {vacancy['area']['name']}, Зарплата: {vacancy['salary']}, Ссылка : {vacancy['alternate_url']}")
        else:
            print("Вакансии не найдены.")

        list_vacancies = Vacancy.cast_to_object_list(vacancies)

if __name__ == "__main__":

    user_interaction()