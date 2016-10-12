#!/usr/bin/python
import pandas_datareader.data as web
import os
from datetime import date, datetime, timedelta
#
datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
todays_date = date.today()   # retreived in YYYY-MM-DD format
n = 365
date_n_days_ago = date.today() - timedelta(days=n)
#Delete file if it exists
my_file = "/home/arsenal/Documents/Stocks/dowStocks.csv"
if os.path.isfile(my_file):
	print("Deleting file now")
	os.remove(my_file)
else:
	print("Couldn't delete file")

#
print("starting Scrapping... Please be patient!")
mylist = ['V', 'VZ', 'XOM', 'CVX', 'TRV', 'IBM', 'CAT', 'UTX', 'NKE', 'MSFT', 'BA', 'INTC', 'MRK', 'KO', 'JPM', 'CSCO', 'JNJ', 'DIS', 'PG', 'MMM', 'MCD', 'GS', 'PFE', 'AAPL', 'GE', 'UNH', 'DD', 'HD', 'WMT', 'AXP']
#
symbols=[]
for yahoo_symbol in mylist:
        stock_data = web.DataReader(yahoo_symbol, 'yahoo', date_n_days_ago, todays_date)
	stock_data['Symbol'] = yahoo_symbol
	symbols.append(stock_data)
	#print(stock_data.head())
	cell= stock_data[['Symbol','Volume', 'Adj Close']]
	#print(cell.head())
	cell.to_csv('/home/arsenal/Documents/Stocks/dowStocks.csv', mode='a', header=False)
print("Scrapping done successfully!")

