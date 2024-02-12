from utils import display_contacts, add_contact, edit_contact, search_contacts


def main():
    while True:
        user_input = input('Введите команду:\nget - для вывода всех контактов\npost - для добавления записей в справочник\n'
                           'patch - для редактирования записей в справочнике\nsearch - для поиска контакта\nquit - для выхода\n').lower()
        if user_input == 'get':
            display_contacts()
        elif user_input == 'post':
            add_contact()
        elif user_input == 'patch':
            edit_contact()
        elif user_input == 'search':
            search_contacts(input('Введите Id, Имя или Фамилию контакта\n'))
        elif user_input == 'quit':
            break
        else:
            print('Некорректная команда. Попробуйте еще раз.\n')

if __name__ == '__main__':
    main()


