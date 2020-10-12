# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:42:57 2020

@author: ManoftheMountains

Desc: Private cryptocurrency investment dashboard functions
"""
#%%

##### FUNCTION RETURNS HISTORICAL DATA

def historical(coin,timefrom,timeto):
    
    # IMPORT REQUIREMENTS
    from pycoingecko import CoinGeckoAPI
    import pandas as pd
    import datetime
    import time
    
    # TIME CONVERSION TO UNIX STAMP
    UNIXtimefrom = time.mktime(datetime.datetime.strptime(timefrom, "%Y-%m-%d").timetuple())
    UNIXtimeto = time.mktime(datetime.datetime.strptime(timeto, "%Y-%m-%d").timetuple())
    
    # DEFINE COINGECKO API (FREE)
    cg = CoinGeckoAPI()
    
    # HISTORICAL DATA API
    history = cg.get_coin_market_chart_range_by_id(id=coin,vs_currency='usd', from_timestamp= UNIXtimefrom, to_timestamp= UNIXtimeto)
      
    # FORMATTING DATAFRAME
    dateList = []
    priceList = []
    for i in history['prices']:
        dateList.append(i[0])
        priceList.append(i[1])
    
    market_capList = []
    for i in history['market_caps']:
        market_capList.append(i[1])
        
    total_volumesList = []
    for i in history['total_volumes']:
        total_volumesList.append(i[1])
    
    df = pd.DataFrame(zip(dateList,priceList,market_capList,total_volumesList) ,columns=['date','usd','market_cap','volume'])
    df['date'] = pd.to_datetime(df['date'],unit='ms')
    df.index = df['date']
    del df['date']

    return df 

#%%

##### FUNCTION COIN LIST TO CSV
def coinlist():
    # IMPORT REQUIREMENTS
    from pycoingecko import CoinGeckoAPI
    import pandas as pd
    
    # QUERY
    cg = CoinGeckoAPI()
    coinlist = cg.get_coins_list()
    
    # TO DATAFRAME
    coindf = pd.DataFrame.from_dict(coinlist)
    
    # TO CSV
    coindf.to_csv('coin_list.csv', sep=',', encoding='utf-8')

#%%
    
##### TESTING
    
time1 = '2019-01-01'
time2 = '2020-09-29'
coin1 = 'bitcoin'

test = historical(coin1,time1,time2)
test['usd'].plot()
