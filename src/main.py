from src.HeadHunterAPI import HeadHunterAPI

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")
print(hh_vacancies)
