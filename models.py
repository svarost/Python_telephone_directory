import csv
from datetime import datetime

f_in_path = 'Dictionary.txt'
f_out_path = 'Dictionary.txt'
# csv_out_path = 'Dictionary_out.csv'
# csv_in_path = 'Dictionary_in.csv'
f_log_path = 'log.txt'

def dictionary_r():
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        data_row=[]
        for row in data_in:
            data_row.append(row.rstrip('\n'))
        # data_in = data_in.readline()#.split('\n')
        # print(data_row)
    return data_row


def dictionary_w(data):
    with open(f_out_path, 'a', encoding='utf-8') as data_out:
        data_out.writelines(' '.join(data)+'\n')
        log_files('добавлена запись',' '.join(data))


def search(search_data):
    data_row=[]
    number=0
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        for n,row in enumerate(data_in,1):
            if search_data.lower() in row.lower():
                data_row.append(row.rstrip('\n'))
                number=n-1
        log_files('поиск',search_data)
        return data_row, number

def delete_data(n):
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        data = data_in.readlines()
    data_del = data[n]
    del data[n]
    log_files('удалена запись',data_del)
    with open(f_in_path, 'w', encoding='utf-8') as data_in:
        data_in.writelines(data)


def log_files(type_action,data):
    with open(f_log_path, 'a', encoding='utf-8') as data_log:
        dt = datetime.now()
        data_log.write(dt.strftime(f'В %m.%d.%Y %H:%M:%S - {type_action} "{data}"\n'))


def quit():
    return False
