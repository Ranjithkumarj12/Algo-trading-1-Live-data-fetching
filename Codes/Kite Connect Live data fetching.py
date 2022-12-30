# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:30:55 2022

@author: jrkumar
"""

import pandas as pd
from kiteconnect import KiteConnect
# for streaming live price quotes (need public token for this)
from kiteconnect import KiteTicker
import logging

# Path where Ticker symbols are stored
path_tickers = (r'C:\Users\jrkumar\OneDrive - Indxx\Desktop\Algo Trading Engine\Inputs - Generic\\')
input_path = (r'C:\Users\jrkumar\OneDrive - Indxx\Desktop\Algo Trading Engine\Arbitrage Strategy\Inputs\\')

# Use api_key to get url, Use url to get request token, Use request token + api_secret to get access token - This is correct
logging.basicConfig(level=logging.DEBUG)

api_key = ''
api_secret = ''
kite = KiteConnect(api_key = api_key)
url_redirect = kite.login_url()
print(url_redirect)

meta_data = kite.generate_session('', api_secret=api_secret)
access_token = kite.set_access_token(meta_data["access_token"])

#Input Tickers
instruments_dict = {}

instruments_df = pd.read_csv(input_path+r'Instruments - Equity.csv')
instrument_symbol_list = instruments_df['tradingsymbol'].dropna().tolist()
instrument_token_list = instruments_df['instrument_token'].dropna().tolist()
instruments_dict = dict(zip(instrument_symbol_list, instrument_token_list))

logging.basicConfig(level=logging.DEBUG)

# Initialise
kws = KiteTicker(api_key, meta_data["access_token"])

def on_ticks(ws,ticks):
    print(ticks)
    print("\n")
    
def on_connect(ws,response):
    ws.subscribe([113921,3525377,
4882689,
1378561,
2561,
3329,
4583169,
5533185,
7707649,
1421057,
1540609,
2550785,
3580673,
1878785,
2553089,
5633,
1805569,
375041,
3478273,
3015425,
3078145,
6401,
912129,
3861249,
4452353,
2615553,
5058817,
63489,
8705,
1267969,
3792129,
3774721,
4617985,
10241,
2511361,
2903809,
867585,
361473,
2834433,
])
    ws.set_mode(ws.MODE_LTP,[113921,3525377,
4882689,
1378561,
2561,
3329,
4583169,
5533185,
7707649,
1421057,
1540609,
2550785,
3580673,
1878785,
2553089,
5633,
1805569,
375041,
3478273,
3015425,
3078145,
6401,
912129,
3861249,
4452353,
2615553,
5058817,
63489,
8705,
1267969,
3792129,
3774721,
4617985,
10241,
2511361,
2903809,
867585,
361473,
2834433,
])
    
kws.on_ticks = on_ticks
kws.on_connect = on_connect

kws.connect()

