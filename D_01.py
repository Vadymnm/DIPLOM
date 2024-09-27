import csv
import os
import time, datetime


list = os.listdir("trades")
print(len(list), list)
print()


if os.path.exists('table.csv'):
    os.remove('table.csv')

class StockManager():
    def __init__(self):
        self.list = list
        super().__init__()

    def get_data1(self, path):
        ticker_list = []
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                ticker_list.append(row)
        ticker_price_list = []
        for j in range(1, len(ticker_list)):
            ticker_price_list.append(float(ticker_list[j][2]))
        max_price = max(ticker_price_list)
        min_price = min(ticker_price_list)
        average_price = round((max_price + min_price) / 2, 2)
        volatility = round(((max_price - min_price) / average_price) * 100, 2)
        x = (str(path))[14:18]
        table = [x, average_price, volatility]
        # --------------------------------------------------
        time.sleep(0.2)  # имитация задержки обмена данными
        with open('table.csv', 'a', newline='') as f:
            csv.writer(f).writerow(table)

        # --------------------------------------------------

    def read_file(self):
        res_table = []
        with open('table.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                res_table.append(row)
    #    print(len(res_table), res_table)
        return res_table

    def zero_volat(self,table):
        self.table = table
        zero_list = []
        for i in range(len(self.table)):
            if (self.table[i][2]) == '0.0':
                zero_list.append(self.table[i])
        print('==== Нулевая волатильность:', len(zero_list),'позиций ====')
        for i in range(len(zero_list)):
            print(zero_list[i][0], end=', ')
        print()
#        return zero_list

    def min_volat(self, table):
        self.table = table
        no_zero_list = []
        for i in range(len(self.table)):
            if (self.table[i][2]) != '0.0':
                no_zero_list.append(self.table[i])
        no_zero_list.sort(key=lambda x: float(x[2]))
        print('==== 3 позиции с минимальной волатильностью: ====')
        for i in range(2,-1,-1):
            print(no_zero_list[i][0],' - ', no_zero_list[i][2])

    def max_volat(self, table):
        self.table = table
        no_zero_list = []
        for i in range(len(self.table)):
            if (self.table[i][2]) != '0.0':
                no_zero_list.append(self.table[i])
        no_zero_list.sort(key=lambda x: float(x[2]))
        print('==== 3 позиции с максимальной волатильностью: ==== ')
        for i in range(-1,-4,-1):
            print(no_zero_list[i][0],' - ', no_zero_list[i][2])


# *************************************************************


list = os.listdir("trades")     # формирование путей к файлам
for i in range(len(list)):
    list[i] = 'trades/' + list[i]

manager = StockManager()

start = datetime.datetime.now()

for i in range(len(list)):
    manager.get_data1(list[i])

end = datetime.datetime.now()
print('Время подготовки данных: ',end-start)
# ******************************************

start = datetime.datetime.now()

table = manager.read_file()
manager.zero_volat(table)
manager.min_volat(table)
manager.max_volat(table)

end = datetime.datetime.now()
print('Время анализа данных: ', end-start)


