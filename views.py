

def print_greeting():
    print('Телефонный справочник\n')
    # choos_action()


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, phone_number, note]

    
def print_all(data):
        print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Описание".center(20))
        print("-"*85)        
        for i in range(len(data)):
            st=[l for l in data[i].split()]
            for el in st:
                print(el.center(20), end='')
            print()
            # print(data[0+l*4].center(20), data[1+i*4].center(20), data[2+i*4].center(15), data[3+i*4].center(30))
            # print((data[i]))
        print("-"*85)

def input_search():
    return input("Введите строку поиска: ") # ищет любое вхождение (даже несколько символов)
