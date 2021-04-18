import okex.okex_python_sdk_api.okex.spot_api as spot
import numpy as np
import os
import pandas as pd

okex_api_key = os.environ['OKEX_API_KEY']
okex_api_secret = os.environ['OKEX_SECRET']
okex_passphrase = os.environ['OKEX_PASSPHRASE']


def get_all_tickers(api_key=okex_api_key, api_secret=okex_api_secret, api_passphrase=okex_passphrase):
    spot_api = spot.SpotAPI(api_key, api_secret, api_passphrase, False)

    all_tickers_data = spot_api.get_ticker()
    tickers = []

    for ticker_data in all_tickers_data:
        tickers.append(ticker_data['instrument_id'])

    return np.array(tickers)


def get_all_coins(api_key=okex_api_key, api_secret=okex_api_secret, api_passphrase=okex_passphrase):
    spot_api = spot.SpotAPI(api_key, api_secret, api_passphrase, False)

    all_coins_data = spot_api.get_coin_info()
    coins = []

    for ticker_data in all_coins_data:
        coins.append(ticker_data['base_currency'])

    return np.array(coins)


def create_dataframe_with_unified_names(tickers=get_all_tickers()):
    df = pd.DataFrame(columns=['name'])
    df.index.names = ['unified name']

    for ticker in tickers:
        ticker_split = ticker.split('-')
        uni_name = ticker_split[0] + '.' + ticker_split[1]

        df.at[uni_name, 'name'] = ticker

    return df
