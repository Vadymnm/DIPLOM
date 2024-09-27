import csv
import os
import datetime, time
from threading import Thread


if os.path.exists('table.csv'): # удаление файла table.csv
    os.remove('table.csv')

print('-------------------------------------------------------**')
class StockManager(Thread):
    def __init__(self, list):
        self.list = list
        super().__init__()

    def get_data_(self, path):  # - вычисления для одного тикера
        self.path = path
        ticker_list = []
        with open(self.path, 'r') as file:
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
        time.sleep(0.2)         # имитация задержки обмена данными
        with open('table.csv', 'a', newline='') as f:
            csv.writer(f).writerow(table)


    def run(self):
        self.list = list
        self.get_data_(self.list[i])
    # --------------------------------------------------

#print('*********************************************************')

start = datetime.datetime.now()

list = os.listdir("trades")
for i in range(len(list)):
    list[i] = 'trades/' + list[i]

print('*********************************************************')

start = datetime.datetime.now()

threads = []
for i in range(len(list)):
    thread = StockManager(list[i])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = datetime.datetime.now()
print('Tatal processing time =', end - start)
print('*** table.csv  file  created !!! ***')