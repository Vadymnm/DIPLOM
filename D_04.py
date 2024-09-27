import csv
import os
import datetime
import asyncio


if os.path.exists('table.csv'):
    os.remove('table.csv')

print('-------------------------------------------------------**')

async def get_data_(path):  # - вычисления для одного тикера
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
    await asyncio.sleep(0.2)        # имитация задержки обмена данными
    with open('table.csv', 'a', newline='') as f:
        csv.writer(f).writerow(table)


# ---------------------------------------

async def main():
    for i in range(0, len(list), 8):
        await asyncio.gather(get_data_(list[i]), get_data_(list[i+1]),
                             get_data_(list[i+2]), get_data_(list[i + 3]),
                             get_data_(list[i+4]), get_data_(list[i + 5]),
                             get_data_(list[i + 6]), get_data_(list[i + 7]))

print('***********************************************')

list = os.listdir("trades")
for i in range(len(list)):
    list[i] = 'trades/' + list[i]
print(len(list), 'list... = ', list)
print(' -- path list created --')


if __name__ == '__main__':
    start = datetime.datetime.now()
    asyncio.run(main())
    end = datetime.datetime.now()

print('Total processing time =', end - start)
print('*** table.csv  file  created !!! ***')