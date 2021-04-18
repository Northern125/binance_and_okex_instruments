import binance_data
import okex_data
from aggregation_of_all_tickers import create_table_with_all_tickers

if __name__ == '__main__':
    df = create_table_with_all_tickers(binance_tickers=binance_data.get_all_tickers(),
                                       okex_tickers=okex_data.get_all_tickers())
    df.to_csv('all_tickers.csv')
