"""
Example to use python csv (Comma Separate Value) module

Data is saved at:
    C:\Work\data\Google Stock Market Data - google_stock_data.csv.csv
"""
import csv
from datetime import datetime


path = 'C:\\Work\\data\\Google Stock Market Data - google_stock_data.csv.csv'
file = open(path, newline='')

#normal read file without csv module
# lines = [line for line in file]
# print(lines[0])
# print(lines[1])

reader = csv.reader(file)
header = next(reader)   #read the header

data = []
for row in reader: #read the remaing data
    #row = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    data_set = [
        datetime.strptime(row[0], '%m/%d/%Y'),
        float(row[1]),
        float(row[2]),
        float(row[3]),
        float(row[4]),
        int(row[5]),
        float(row[6]),
    ]
    data.append(data_set)

# compute and store the daily  stock return
return_path = 'C:\\Work\\data\\Google_daily_return.csv'
return_file = open(return_path, mode='w')
writer = csv.writer(return_file)
writer.writerow(['Date', 'Return'])

for i in range(len(data)-1):
    today_date = data[i][0]
    today_price = data[i][-1]
    yesterday_price = data[i+1][-1]
    return_rate = (today_price - yesterday_price) / yesterday_price
    writer.writerow([datetime.strftime(today_date, '%m/%d/%Y'), return_rate])


