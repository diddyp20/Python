#!/usr/bin/python
import os
import pandas_datareader.data as web
from datetime import date, datetime, timedelta
#
datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
todays_date = date.today()   # retreived in YYYY-MM-DD format
n = 365
date_n_days_ago = date.today() - timedelta(days=n)
#Delete file if it exists
my_file = "/home/arsenal/Documents/Stocks/SNPstocks2.csv"
if os.path.isfile(my_file):
	print("Deleting file now")
	os.remove(my_file)
else:
	print("Couldn't delete file")

#
print("starting Scrapping... Please be patient!")
mylist = ['A','AA','AAL','AAP','AAPL','ABBV','ABC',	'ABT', 'ACN', 'ADBE',	'ADI',	'ADM',	'ADP',	'ADS',	'ADSK',	'AEE',	'AEP',	'AES',	'AET',	'AFL',	'AGN',	'AIG',	'AIV',	'AIZ',	'AJG',	'AKAM',	'ALB',	'ALK',	'ALL',	'ALLE',	'ALXN',	'AMAT',	'AME',	'AMG',	'AMGN',	'AMP',	'AMT',	'AMZN',	'AN',	'ANTM',	'AON',	'APA',	'APC',	'APD',	'APH',	'ASIX',	'ATVI',	'AVB',	'AVGO',	'AVY',	'AWK',	'AXP',	'AYI',	'AZO',	'BA',	'BAC',	'BAX',	'BBBY',	'BBT',	'BBY',	'BCR',	'BDX',	'BEN',	'BHI',	'BIIB',	'BK',	'BLK',	'BLL',	'BMY',	'BSX',	'BWA',	'BXP',	'C',	'CA',	'CAG',	'CAH',	'CAT',	'CB',	'CBG',	'CBS',	'CCI',	'CCL',	'CELG',	'CERN',	'CF',	'CFG',	'CHD',	'CHK',	'CHRW',	'CHTR',	'CI',	'CINF',	'CL',	'CLX',	'CMA',	'CMCSA',	'CME',	'CMG',	'CMI',	'CMS',	'CNC',	'CNP',	'COF',	'COG',	'COH',	'COL',	'COO',	'COP',	'COST',	'COTY',	'CPB',	'CRM',	'CSCO',	'CSRA',	'CSX',	'CTAS',	'CTL',	'CTSH',	'CTXS',	'CVS',	'CVX',	'CXO',	'D',	'DAL',	'DD',	'DE',	'DFS',	'DG',	'DGX',	'DHI',	'DHR',	'DIS',	'DISCA',	'DISCK',	'DLPH',	'DLR',	'DLTR',	'DNB',	'DOV',	'DOW',	'DPS',	'DRI',	'DTE',	'DUK',	'DVA',	'DVN',	'EA',	'EBAY',	'ECL',	'ED',	'EFX',	'EIX',	'EL',	'EMN',	'EMR',	'ENDP',	'EOG',	'EQIX',	'EQR',	'EQT',	'ES',	'ESRX',	'ESS',	'ETFC',	'ETN',	'ETR',	'EW',	'EXC',	'EXPD',	'EXPE',	'EXR',	'F',	'FAST',	'FB',	'FBHS',	'FCX',	'FDX',	'FE',	'FFIV',	'FIS',	'FISV',	'FITB',	'FL',	'FLIR',	'FLR',	'FLS',	'FMC',	'FOX',	'FOXA',	'FRT',	'FSLR',	'FTI',	'FTR',	'FTV',	'GD',	'GE',	'GGP',	'GILD',	'GIS',	'GLW',	'GM',	'GOOG',	'GOOGL',	'GPC',	'GPN',	'GPS',	'GRMN',	'GS',	'GT',	'GWW',	'HAL',	'HAR',	'HAS',	'HBAN',	'HBI',	'HCA',	'HCN',	'HCP',	'HD',	'HES',	'HIG',	'HOG',	'HOLX',	'HON',	'HP',	'HPE',	'HPQ',	'HRB',	'HRL',	'HRS',	'HSIC',	'HST',	'HSY',	'HUM',	'IBM',	'ICE',	'IFF',	'ILMN',	'INTC',	'INTU',	'IP',	'IPG',	'IR',	'IRM',	'ISRG',	'ITW',	'IVZ',	'JBHT',	'JCI',	'JEC',	'JNJ',	'JNPR',	'JPM',	'JWN',	'K',	'KEY',	'KHC',	'KIM',	'KLAC',	'KMB',	'KMI',	'KMX',	'KO',	'KORS',	'KR',	'KSS',	'KSU',	'L',	'LB',	'LEG',	'LEN',	'LH',	'LKQ',	'LLL',	'LLTC',	'LLY',	'LM',	'LMT',	'LNC',	'LNT',	'LOW',	'LRCX',	'LUK',	'LUV',	'LVLT',	'LYB',	'M',	'MA',	'MAC',	'MAR',	'MAS',	'MAT',	'MCD',	'MCHP',	'MCK',	'MCO',	'MDLZ',	'MDT',	'MET',	'MHK',	'MJN',	'MKC',	'MLM',	'MMC',	'MMM',	'MNK',	'MNST',	'MO',	'MON',	'MOS',	'MPC',	'MRK',	'MRO',	'MS',	'MSFT',	'MSI',	'MTB',	'MTD',	'MU',	'MUR',	'MYL',	'NAVI',	'NBL',	'NDAQ',	'NEE',	'NEM',	'NFLX',	'NFX',	'NI',	'NKE',	'NLSN',	'NOC',	'NOV',	'NRG',	'NSC',	'NTAP',	'NTRS',	'NUE',	'NVDA',	'NWL',	'NWS',	'NWSA',	'O',	'OI',	'OKE',	'OMC',	'ORCL',	'ORLY',	'OXY',	'PAYX',	'PBCT',	'PBI',	'PCAR',	'PCG',	'PCLN',	'PDCO',	'PEG',	'PEP',	'PFE',	'PFG',	'PG',	'PGR',	'PH',	'PHM',	'PKI',	'PLD',	'PM',	'PNC',	'PNR',	'PNW',	'PPG',	'PPL',	'PRGO',	'PRU',	'PSA',	'PSX',	'PVH',	'PWR',	'PX',	'PXD',	'PYPL',	'QCOM',	'QRVO',	'R',	'RAI',	'RCL',	'REGN',	'RF',	'RHI',	'RHT',	'RIG',	'RL',	'ROK',	'ROP',	'ROST',	'RRC',	'RSG',	'RTN',	'SBUX',	'SCG',	'SCHW',	'SE',	'SEE',	'SHW',	'SIG',	'SJM',	'SLB',	'SLG',	'SNA',	'SNI',	'SO',	'SPG',	'SPGI',	'SPLS',	'SRCL',	'SRE',	'STI',	'STJ',	'STT',	'STX',	'STZ',	'SWK',	'SWKS',	'SWN',	'SYF',	'SYK',	'SYMC',	'SYY',	'T',	'TAP',	'TDC',	'TDG',	'TEL',	'TGNA',	'TGT',	'TIF',	'TJX',	'TMK',	'TMO',	'TRIP',	'TROW',	'TRV',	'TSCO',	'TSN',	'TSO',	'TSS',	'TWX',	'TXN',	'TXT',	'UA','UAL',	'UDR',	'UHS',	'ULTA',	'UNH',	'UNM',	'UNP',	'UPS',	'URBN',	'URI',	'USB',	'UTX',	'V',	'VAR',	'VFC',	'VIAB',	'VLO',	'VMC',	'VNO',	'VRSK',	'VRSN',	'VRTX',	'VSM',	'VTR',	'VZ',	'WAT',	'WBA',	'WDC',	'WEC',	'WFC',	'WFM',	'WHR',	'WLTW',	'WM',	'WMB',	'WMT',	'WRK',	'WU',	'WY',	'WYN',	'WYNN',	'XEC',	'XEL',	'XL',	'XLNX',	'XOM',	'XRAY',	'XRX',	'XYL',	'YHOO',	'YUM',	'ZBH',	'ZION',	'ZTS']
#
symbols=[]
for yahoo_symbol in mylist:
        stock_data = web.DataReader(yahoo_symbol, 'yahoo', date_n_days_ago, todays_date)
	stock_data['Symbol'] = yahoo_symbol
	symbols.append(stock_data)
	#print(stock_data.head())
	cell= stock_data[['Symbol','Volume', 'Adj Close']]
	#print(cell.head())
	cell.to_csv('/home/arsenal/Documents/Stocks/SNPstocks2.csv', mode='a', header=False)
#concatenate
print("Scrapping done successfully!")

