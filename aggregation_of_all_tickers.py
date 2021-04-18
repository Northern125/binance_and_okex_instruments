import numpy as np

import binance_data
import okex_data


def create_table_with_all_tickers(binance_tickers=None, okex_tickers=None):
    binance_tickers = np.unique(binance_tickers)
    okex_tickers = np.unique(okex_tickers)

    columns = ['binance name', 'okex name']

    binance_df_and_bt = binance_data.create_dataframe_with_unified_names(tickers=binance_tickers)
    binance_df = binance_df_and_bt['dataframe']

    okex_df = okex_data.create_dataframe_with_unified_names(tickers=okex_tickers)

    table = binance_df.merge(okex_df, how='outer', left_index=True, right_index=True)
    table.columns = columns
    table.index.names = ['unify name']
    table.sort_index(inplace=True)

    return table
