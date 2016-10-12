#!/usr/bin/python
import pandas as pd
import datetime as dt
import numpy as np
import sys
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

#Delete Ouput file if it exist
my_file = "/home/arsenal/PycharmProjects/untitled/Report.txt"
if os.path.isfile(my_file):
	print("Deleting file now")
	os.remove(my_file)
else:
	print("Couldn't delete file")

# open a the CSV file created
dataset = pd.read_csv('/home/arsenal/Documents/Stocks/SNPstocks2.csv', header=None,
                      names=['Date', 'Sticker', 'Volume', 'Price'], index_col=False)
sys.stdout=open("Report.txt","w")

#Function
def tableGenration (baseline):
# variables List
    base = 1
    base5 = baseline
    increment = 0
# Convert Date in Date format
    dataset['Date'] = pd.to_datetime(dataset['Date'])

# Sort the dataset
    dataset.sort_values(['Date', 'Sticker'], ascending=[False, True], inplace=True)

# Get today's date
    todayDate = dt.date.today()
# Get all the rows that are from today
    TodayStocks = dataset[dataset['Date'] >= todayDate ] #- dt.timedelta(days=base)]
    countSize = len(TodayStocks)
# if size is zero
# if date does not exist, use the next available one
    if countSize <= 0:
        increment += 1
        while countSize <= 0:
            base += increment
            TodayStocks = dataset[dataset['Date'] == todayDate - dt.timedelta(days=base)]
            countSize = len(TodayStocks)
            #print "Dataframe 1 has been updated with another Date"

    # Get the dataframe for last 5 days Stocks
    last5Days = dataset[dataset['Date'] == todayDate - dt.timedelta(days=base5)]
    countSize2 = len(last5Days)

    # if the Day is not available, use the next available one
    if countSize2 <= 0:
        increment += 1
        while countSize2 <= 0:
            base5 += increment
            last5Days = dataset[dataset['Date'] == todayDate - dt.timedelta(days=base5)]
            countSize2 = len(last5Days)
            #print "Dataframe 2 has been updated with another Date"

    # rename column in 2nd Dataframe
    newLast5Days = last5Days.rename(index=str, columns={'Date': 'Date2', 'Volume': 'Volume2', 'Price': 'Price2'})

    #display today top 5 and bottom 5
    #sort first
    newToday = TodayStocks
    newToday.sort_values(['Price'], ascending=False, inplace=True)
    # merging the dataset
    last5DaysDF = pd.merge(TodayStocks, newLast5Days, on='Sticker')
    # Drop Dates columns from dataframe
    last5DaysDF.drop('Date', axis=1, inplace=True)
    last5DaysDF.drop('Date2', axis=1, inplace=True)

    # Calculate the deltas
    last5DaysDF['Delta'] = ((last5DaysDF['Price'] - last5DaysDF['Price2']) / last5DaysDF['Price2']) * 100
    last5DaysDF['Delta1'] = (np.around(last5DaysDF['Delta'], decimals=2))
    last5DaysDF['Price'] = (np.around(last5DaysDF['Price'], decimals=2))
    last5DaysDF['Price'] = '$' + ((last5DaysDF['Price']).apply(str))
    last5DaysDF['Delta1'] = ((last5DaysDF['Delta1']).apply(str)) + '%'
    # last5DaysDF['Delta'] = ((np.around(last5DaysDF['Delta'],decimals=2)).apply(str))+'%'

    # Sort in descending order
    last5DaysDF.sort_values('Delta', ascending=False, inplace=True)
    # Save Top 5 and Bottom 5
    TopFive = last5DaysDF.head(5)
    bottomFive = last5DaysDF.tail(5)
    bottomFive.sort_values('Delta', ascending=True, inplace=True)

    # drop Unwanted Columns

    newTopFive = TopFive[['Sticker', 'Volume', 'Price', 'Delta1']]
    newBottomFive = bottomFive[['Sticker', 'Volume', 'Price', 'Delta1']]
    newTopFive = newTopFive.rename(index=str, columns={'Delta1': 'Delta'})
    newBottomFive = newBottomFive.rename(index=str, columns={'Delta1': 'Delta'})

    print(" ")
    print("              TOP 5 WINNERS STOCKS        ")
    print(" ")
    print(newTopFive.head(5))
    print(" ")
    print("              TOP 5 LOSERS STOCKS        ")
    print(" ")
    print(newBottomFive.head(5))
    # Convert to htlm
    # TopFive.set_index('Sticker', inplace=True)
    TopFive.to_html('/home/arsenal/Documents/Stocks/topFive.html')
    bottomFive.to_html('/home/arsenal/Documents/Stocks/BottomFive.html')
    return

##Send Email
print("       **************************************")
print "                     ", str(dt.date.today())
print("       **************************************")
print(" ")
print("###########################################################")
print("              Stocks Last 2 Days         ")
print "         From ",str(dt.date.today() - dt.timedelta(1))," To ", str(dt.date.today())
tableGenration(2)
print(" ")
print("###########################################################")
print("              Stocks Last Five Days             ")
print "        From ",str(dt.date.today() - dt.timedelta(5))," To ", str(dt.date.today())
tableGenration(5)
print(" ")
print("###########################################################")
print("             Stocks Last Fifteen Days                           ")
print "        From ",str(dt.date.today() - dt.timedelta(15))," To ", str(dt.date.today())
tableGenration(15)
print(" ")
print("###########################################################")
print("             Stocks Last Thirty Days                        ")
print "        From ",str(dt.date.today() - dt.timedelta(30))," To ", str(dt.date.today())
tableGenration(30)
print(" ")
print("###########################################################")
sys.stdout.close()

fromaddr = "borgodo1@gmail.com"
toaddr="bndidier@gmail.com"
msg= MIMEMultipart('related')
msg['from'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Stock Report"

msg.preamble = 'Multipart massage.\n'

part = MIMEText("Hi, please find the attached file")
msg.attach(part)

part = MIMEApplication(open("/home/arsenal/PycharmProjects/untitled/Report.txt", "rb").read())
part.add_header('Content-Disposition', 'attachment', filename='Report.txt')
msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("borgodo1@gmail.com", "@Sophie1")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()