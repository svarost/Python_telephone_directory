from prettytable import PrettyTable
import os


def print_greeting():
    print('Телефонный справочник\n')
    # choos_action()


def input_data() -> str:
    invites = ['Введите фамилию: ', 'Введите имя: ', 'Введите номер контакта: ', 'Введите категорию контакта: ']

    contact = []
    for item in invites:
        temp = input(item).replace(" ", "")
        contact.append(temp if len(temp) != 0 else 'None')
    return contact


def print_all(data):
    th = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    table = PrettyTable(th)
    data_list = list(map(lambda item: [el for el in item.split()], data))
    table.add_rows(data_list)
    table.add_autoindex("№")
    print(table)


def input_search():
    return input("Введите строку поиска: ")  # ищет любое вхождение (даже несколько символов)
