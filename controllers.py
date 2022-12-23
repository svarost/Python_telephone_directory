import models
import views
import os


def greeting():
    # models.init(get_val)
    views.print_greeting()
    # views.choos_action()


def choice_action():
    print('Выберите действие:\n')
    print('1.Добавить запись.\n2.Полный список.\n3.Поиск.\n4.Удалить запись.\n'
        + '5.Экспорт в CSV\n6.Экспорт в CSV (Excel)\n7.Выход')
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
            print('Удалить запись') 
            models.delete()

        case '5':
            print('Экспорт телефонной книги в CSV')
            models.export_to_csv()

        case '6':
            print('Экспорт телефонной книги в CSV (Excel)')
            models.export_to_csv("Excel")

        case '7':
            print('Выход')
            exit()
