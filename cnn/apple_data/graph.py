import pandas as pd
import quandl
import numpy as np
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from datetime import timedelta, date, datetime


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


data=pd.read_csv('prediction.csv')
label=data['Sentiment']

start_date = date(2015, 1, 1)
start= start_date.strftime("%Y-%m-%d")
end_date = date(2016, 12, 31)
end= end_date.strftime("%Y-%m-%d")
total_day = (end_date-start_date).days
print("Total",total_day,"days.")

day=0
list_date=[]
list_sentiment=np.zeros(total_day)
list_count=np.zeros(total_day)
for single_date in daterange(start_date, end_date):
    date=single_date.strftime("%Y/%m/%d")
    print(date)
    list_date.append(single_date)
    for i,j in data.loc[pd.to_datetime(data['Date'])==pd.to_datetime(date)].iterrows():
        if(j['Sentiment']==1):
            list_sentiment[day]+=1
        list_count[day]+=1
    day+=1
list_average=list_sentiment/list_count
print(list_sentiment,list_count)

stock='AAPL'
quandl.ApiConfig.api_key = 'AH_8yF2qo1ShWwMn_uBr'
print(stock,start,end)
stock_data = quandl.get_table('WIKI/PRICES',
                        ticker = [stock], date = { 'gte': start, 'lte': end })
print(stock_data)
stock_data.from_records(stock_data)
trade_date=np.array(stock_data.loc[stock_data['ticker'] == stock]['date'])
apple=np.array(stock_data.loc[stock_data['ticker'] == stock]['close'])

#
# plt.plot(trade_date,apple,'r-')
# plt.title('AAPL Stock Price')
# plt.show()
# plt.plot(list_date,list_sentiment,'b-')
# plt.plot(list_date,list_count,'g-')
# plt.title('Daily positive news (blue) and Daily total news (green)')
# plt.show()
# plt.plot(list_date,list_average,'y-')
# plt.title('Daily average sentiment')
# plt.show()

fig, ax1 = plt.subplots()
ax1.plot(trade_date, apple, 'b-')
ax1.set_xlabel('AAPL Stock Price')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Price', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(list_date, list_average, 'r-')
ax2.set_ylabel('Sentiment', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()