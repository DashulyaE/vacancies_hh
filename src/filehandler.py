class JSONSaver:
    # def json_save(self, list_object):
    #     """Записывает информацию в файл с фильтром на дубликаты"""
    #     old_vacancies = self.json_give()
    #     new_list = []
    #     if old_vacancies == []:
    #         for vacancy_new in list_object:
    #             new_list.extend(vacancy_new.vacancy_dict)
    #         old_vacancies.extend(new_list)
    #     else:
    #         for vacancy in old_vacancies:
    #             for index, new_vacancy in enumerate(list_object):
    #                 if vacancy.get('name', 'pass') == new_vacancy.name:
    #                     list_object.pop(index)
    #         for vacancy_new in list_object:
    #             old_vacancies.extend(vacancy_new.vacancy_dict)
    #
    #     with open(self.__filename, "w", encoding="utf-8") as file:
    #         json.dump(old_vacancies, file, indent=4, ensure_ascii=False)
    pass
