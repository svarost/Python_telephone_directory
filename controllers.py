import models
import views

def greeting():
    # models.init(get_val)
    views.print_greeting()
    # views.choos_action()
def choice_action():
    print('Выберите действие:\n')
    print('1.Добавить запись.\n2.Полный список.\n3.Поиск.\n4.Удалить запись.\n5.Выход')
    choos=input('Ваш выбор: ')
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
            data,n=models.search(views.input_search())
            views.print_all(data)

        case '4':
            print('Удалить запись')# при нахождении нескольких совпадение удаляет последнее
            data,n=models.search(views.input_search())
            views.print_all(data)
            models.delete_data(n)
        
        case '5':
            print('Выход')
            exit()
            
    
