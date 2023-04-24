# Задача 38:
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# def show_menu() -> int:
# print("\nВыберите необходимое действие:\n"
# "1. Отобразить весь справочник\n"
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
# "4. Добавить абонента в справочник\n"
# "5. Сохранить справочник в текстовом формате\n"
# "6. Закончить работу")
# choice = int(input())
# return choice

# Homework:
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных/
#------------------------------------------
def show_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        book = file.read()
    return book
def find_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('что ищем?: ')
        for i in book:
            if temp in i:
                print(i)
def new_data():
    with open('phonebook.csv', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: ' + '\n'))
def delete_person(name):
    persons = show_data()
    with open('phonebook.csv', "w", encoding="utf8") as file:
        for person in persons:
            if name != person:
                file.write(person)
def change_person(new_name, old_name):
    persons = show_data()
    with open('phonebook.csv', "w", encoding="utf8") as file:
        for person in persons:
            if old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")


while True:
    mode = input('Выберите режим работы справочника' + '\n'
                 + '0-показ файла, 1-поиск данных, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '0':
        print(show_data())
    elif mode == '1':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('кого удаляем?: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        change_person(new_name, old_name)
    elif mode == '5':
        break
    else:
        print('No mode')