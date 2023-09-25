# Выбор команды.
def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep='\n')
    choice = int(input('Введите команду: '))
    return choice

# Распечатывает справочник.


def print_result(book):
    for i in range(len(book)):
        print(book[i])

# Поиск по фамилии и распечатка данных конкретного человека.


def find_by_lastname(book, lastName):
    for i in range(len(book)):
        if lastName == book[i]['Фамилия']:
            resalt = book[i]['Телефон']
    return resalt

# Изменение номера телефона по имени или фамилии человека.


def change_number(book, lastName, numTelefon):
    for i in range(len(book)):
        if lastName == book[i]['Фамилия'] or lastName == book[i]['Имя']:
            book[i]['Телефон'] = numTelefon
    return book

# Удаление записи по имени или фамилии человека.


def delete_by_lastname(book, lastName):

    for i in range(len(book)):
        if lastName == book[i]['Фамилия'] or lastName == book[i]['Имя']:
            r = i
    book.pop(r)
    return book


# Функция запрашивающая коману и запускающая её.


def work_with_phonebook():

    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(
                f'Телефон: {find_by_lastname(phone_book, last_name)}')
        elif choice == 3:
            last_name = input('Введите Фамилию или Имя: ')
            new_number = input('Введите новый телефон: ')
            print_result(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            lastname = input('Введите Фамилию или Имя: ')
            print_result(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.csv', phone_book)

        choice = show_menu()

# Чтение файла.


def read_csv(filename):

    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

# Перезапись файла.


def write_txt(filename, phone_book):

    with open('phonebook.csv', 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')


# Запуск прораммы.
work_with_phonebook()
