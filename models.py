
f_in_path = 'Dictionary.txt'
f_out_path = 'Dictionary.txt'


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


def search(search_data):
    data=[]
    number=0
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        for n,line in enumerate(data_in,1):
            if search_data in line:
                data+=line.split()
                number=n-1
        # data_row=[]
        # for row in data_in:
        #     data_row.append(row.rstrip('\n'))
        return data, number

def delete_data(n):
    with open(f_in_path, 'r', encoding='utf-8') as data_in:
        data = data_in.readlines()
    del data[n]

    with open(f_in_path, 'w', encoding='utf-8') as data_in:
        data_in.writelines(data)

def quit():
    return False
    # return data

# print(delete_data())