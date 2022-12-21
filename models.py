from prettytable import PrettyTable
import os

import views

f_in_path = 'Dictionary.txt'
f_out_path = 'Dictionary.txt'
f_out_path1 = 'Dictionary1.txt'


def dictionary_r():
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        data_row = []
        for row in data_in:
            data_row.append(row.rstrip('\n'))
        # data_in = data_in.readline()#.split('\n')
        # print(data_row)
    return data_row


def dictionary_w(data):
    with open(f_out_path, 'a', encoding='utf-8') as data_out:
        data_out.writelines(' '.join(data) + '\n')


def search(search_data: str):
    data = []
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        for n, line in enumerate(data_in, 1):
            if search_data.upper() in line.upper():
                data.append(line)
        return data


def delete_data(n):
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        data = data_in.readlines()
    del data[n]

    with open(f_in_path, 'w', encoding='utf-8') as data_in:
        data_in.writelines(data)


def quit():
    return False
    # return data


def delete():
    data = []
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        for n, line in enumerate(data_in, 1):
            data.append(line)
    os.system('cls||clear')
    table = contacts_to_table(data)
    print(table)
    del_row = int(input('Укажите порядковый номер контакта, который необходимо удалить: ')) - 1
    table.del_row(del_row)
    print(table)
    table.del_column("№ по порядку")
    lines = table.get_string(header = False, border = False)
    lists = [[i for i in line.strip().split()] for line in lines.split('\n')]

    with open(f_out_path, 'w', encoding='utf-8') as data_out:
        for cont in lists:
            data_out.write(' '.join(cont) + '\n')


def contacts_to_table(data):
    th = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    table = PrettyTable(th)
    table.add_rows(list(map(lambda item: [el for el in item.split()], data)))
    table.add_autoindex("№ по порядку")
    return table

# print(delete_data())
