import csv
import datetime


def read_file():
    res_table = []
    with open('table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            res_table.append(row)
    print(len(res_table), res_table)
    return res_table

def zero_volat(table):
    zero_list = []
    for i in range(len(table)):
        if (table[i][2]) == '0.0':
           zero_list.append(table[i])
    print('==== Нулевая волатильность:', len(zero_list),'позиций из ', len(table), ' ====')
    for i in range(len(zero_list)):
        print(zero_list[i][0], end=', ')
    print()
    return zero_list

def min_volat(table):
    no_zero_list = []
    for i in range(len(table)):
        if (table[i][2]) != '0.0':
            no_zero_list.append(table[i])
    no_zero_list.sort(key=lambda x: float(x[2]))
    print('==== 3 позиции с минимальной волатильностью: ====')
    for i in range(2,-1,-1):
        print(no_zero_list[i][0],' - ', no_zero_list[i][2],'%')
    return no_zero_list

def max_volat(table):
    no_zero_list = []
    for i in range(len(table)):
        if (table[i][2]) != '0.0':
            no_zero_list.append(table[i])
    no_zero_list.sort(key=lambda x: (float(x[2])), reverse=True)
    print('==== 3 позиции с максимальной волатильностью: ==== ')
    for i in range(3):
        print(no_zero_list[i][0],' - ', no_zero_list[i][2],'%')
    return no_zero_list


start = datetime.datetime.now()
print('==================')
table = read_file()

end = datetime.datetime.now()
print(end-start)
start = datetime.datetime.now()
#print(table)
print('==================')
zero_volat(table)
min_volat(table)
max_volat(table)

end = datetime.datetime.now()
print('Total time of calculation = ', end-start)
# *************************************************************

