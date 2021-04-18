from binance.client import Client
import numpy as np
import os
import pandas as pd

binance_api_key = os.environ['BINANCE_API_KEY']
binance_api_secret = os.environ['BINANCE_SECRET']


def get_all_tickers(api_key=binance_api_key, api_secret=binance_api_secret):
    client = Client(api_key=api_key, api_secret=api_secret)

    all_tickers_data = client.get_all_tickers()
    tickers = []

    for ticker_data in all_tickers_data:
        tickers.append(ticker_data['symbol'])

    return np.array(tickers)


def get_all_coins(api_key=binance_api_key, api_secret=binance_api_secret):
    client = Client(api_key=api_key, api_secret=api_secret)

    all_coins_data = client.get_all_coins_info()
    coins = []

    for coin_data in all_coins_data:
        coins.append(coin_data['coin'])

    return np.array(coins)


def create_dataframe_with_unified_names(tickers=get_all_tickers(), coins=get_all_coins()):
    df = pd.DataFrame(columns=['name'])
    df.index.names = ['unified name']

    bad_tickers = []

    for ticker in tickers:
        flag = True
        for coin in coins:
            coin_len = len(coin)
            if ticker.startswith(coin) and ticker[coin_len:] in coins:
                uni_name = coin + '.' + ticker[coin_len:]
                df.at[uni_name, 'name'] = ticker
                flag = False

        if flag:
            bad_tickers.append(ticker)

    return {'dataframe': df, 'bad_tickers': bad_tickers}
