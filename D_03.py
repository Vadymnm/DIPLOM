import csv
import multiprocessing
import os
import datetime, time


if os.path.exists('table.csv'):
    os.remove('table.csv')

print('-------------------------------------------------------**')
def get_data_(path):        # - вычисления для одного тикера
    ticker_list = []
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            ticker_list.append(row)
#            print(ticker_list)
    ticker_price_list = []
    for j in range(1, len(ticker_list)):
        ticker_price_list.append(float(ticker_list[j][2]))
    max_price = max(ticker_price_list)
    min_price = min(ticker_price_list)
    #    print('max price = ',max_price, 'min price = ',min_price)
    average_price = round((max_price + min_price) / 2, 2)
    volatility = round(((max_price - min_price) / average_price) * 100, 2)
    x = (str(path))[14:18]
    table = [x, average_price, volatility]
    # --------------------------------------------------
    time.sleep(0.2)             # имитация задержки обмена данными
    with open('table.csv', 'a', newline='') as f:
        csv.writer(f).writerow(table)

# ---------------------------------------

print('*********************************************************')

list = os.listdir("trades")
for i in range(len(list)):
    list[i] = 'trades/' + list[i]

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(get_data_, list)
        end = datetime.datetime.now()
    print('Tatal processing time =', end - start)
    print('*** table.csv  file  created !!! ***')

# *************************************************************

