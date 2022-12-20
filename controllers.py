import models
import views


def greeting():
    # models.init(get_val)
    views.print_greeting()
    # views.choos_action()


def choice_action():
    print('Выберите действие:\n')
    print('1.Добавить запись.\n2.Полный список.\n3.Поиск.\n4.Удалить запись.\n5.Выход')
    choos = input('Ваш выбор: ')
    # print(choos)

    str_dictionary_f = models.dictionary_r()

    match choos:
        case '1':
            print('Добавить запись')
            models.dictionary_w(views.input_data())

        case '2':
            print('Полный список')
            views.print_all(str_dictionary_f)

        case '3':
            print('Поиск')  ## ищет любое вхождение (даже несколько символов)
            data = models.search(views.input_search())
            views.print_all(data)

        case '4':
            print('Удалить запись')  # при нахождении нескольких совпадение удаляет последнее
            data, n = models.search(views.input_search())
            views.print_all(data)
            print(n)
            models.delete_data(n)

        case '5':
            print('Выход')
            exit()

    # if choos == '1':
    #     sep = choice_sep()
    #     import_data(input_data(), sep)
    # elif choos == '2':
    #     data = export_data()
    #     print_data(data)
    # else:
    #     word = input("Введите данные для поиска: ")
    #     data = export_data()
    #     item = search_data(word, data)
    #     if item != None:
    #         print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
    #         print("-"*130)
    #         print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
    #     else:
    #         print("Данные не обнаружены")

# f_in_path = 'Dictionary_in.txt'
# f_out_path = 'Dictionary_out.txt'
# repl='абв'

# def open_r():
#     with open(f_in_path, 'r',encoding='utf-8') as data_in:
#         str1=data_in.read()
#     return str1
# str1=open_r()
# print(str1)


# def open_w(res):
#     with open(f_out_path, 'w',encoding='utf-8') as data_out:
#         data_out.writelines(res)
# open_w(res)
# print(res)


# def view(data):
#     print(data)
