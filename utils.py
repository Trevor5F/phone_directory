import json
from pprint import pprint

SPRAVOCHNIK_FILE = "справочник.json"


#  Выводит все контакты
def display_contacts(page_number: int = 1, page_size: int = 2):
    with open(SPRAVOCHNIK_FILE, "r", encoding='utf-8') as file:
        contacts = json.load(file)
        contacts_list = list(contacts.items())  # Преобразуем словарь в список кортежей
    # Вывод постранично записей из справочника на экран
    start = (page_number - 1) * page_size
    end = start + page_size
    contacts_to_display = contacts_list[start:end]
    for contact in contacts_to_display:
        pprint(contact)
        print()

    print("\nНажмите Enter для пролистывания страницы и 'b' чтобы вернуться назад или введите 'q' для выхода.")
    user_input = input()
    if user_input == "":
        display_contacts(page_number + 1, page_size)
    elif user_input == "b":
        display_contacts(page_number - 1, page_size)
    elif user_input == "q":
        return
    else:
        print('Неизвестная команда')
        display_contacts(page_number, page_size)


#  Для добавления записей в справочник
def add_contact():
    try:
        with open(SPRAVOCHNIK_FILE, "r", encoding='utf-8') as file:
            contacts = json.load(file)
    # Если файла нет, создаёт его.
    except FileNotFoundError:
        contacts = {}

    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    organization = input("Введите название организации: ")
    work_phone = input("Введите рабочий телефон: ")
    personal_phone = input("Введите личный телефон: ")

    new_contact = {

        "Фамилия": surname,
        "Имя": name,
        "Отчество": patronymic,
        "Название организации": organization,
        "Рабочий телефон": work_phone,
        "Личный телефон": personal_phone}

    contacts[len(contacts) + 1] = new_contact

    with open(SPRAVOCHNIK_FILE, "w", encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

    print("Контакт успешно добавлен.")


#  Для редактирования записей в справочнике
def edit_contact():
    with open(SPRAVOCHNIK_FILE, "r", encoding='utf-8') as file:
        contacts = json.load(file)

    print("Введите номер контакта для редактирования: ")
    user_input = input()

    if user_input not in contacts:
        print("Контакт с таким номером не найден.")
        return

    contact_to_edit = contacts[user_input]

    print("Введите новые значения для полей (для пропуска поля оставьте пустым):")

    new_last_name = input(f"Фамилия ({contact_to_edit['Фамилия']}): ")
    if new_last_name:
        contact_to_edit["Фамилия"] = new_last_name.title()

    new_first_name = input(f"Имя ({contact_to_edit['Имя']}): ")
    if new_first_name:
        contact_to_edit["Имя"] = new_first_name.title()

    new_middle_name = input(f"Отчество ({contact_to_edit['Отчество']}): ")
    if new_middle_name:
        contact_to_edit["Отчество"] = new_middle_name.title()

    new_organization = input(f"Название организации ({contact_to_edit['Название организации']}): ")
    if new_organization:
        contact_to_edit["Название организации"] = new_organization.title()

    new_work_phone = input(f"Рабочий телефон ({contact_to_edit['Рабочий телефон']}): ")
    if new_work_phone:
        contact_to_edit["Рабочий телефон"] = new_work_phone.title()

    new_personal_phone = input(f"Личный телефон ({contact_to_edit['Личный телефон']}): ")
    if new_personal_phone:
        contact_to_edit["Личный телефон"] = new_personal_phone.title()

    # сохраняет отредактированные данные в справочнике контактов
    contacts[user_input] = contact_to_edit

    with open(SPRAVOCHNIK_FILE, "w", encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

    print("Контакт успешно отредактирован.")


# Поиск контакта
def search_contacts(identifier):
    with open(SPRAVOCHNIK_FILE, "r", encoding='utf-8') as file:
        contacts = json.load(file)
    if identifier.isdigit():
        if identifier in contacts:
            pprint(contacts[str(identifier)])
        else:
            print("Контакт с таким ID не найден")
    else:
        found_contacts = [contact for contact in contacts.values() if contact["Имя"] == identifier.title()]
        if found_contacts:
            for contact in found_contacts:
                pprint(contact)
                print()
        else:
            print("Контакт с таким именем не найден")
