import Packages.DataHandler
from Packages.DataHandler.yahooData import yahooData
import pandas as pd
import os

if __name__ == '__main__':
    tickerListPath = os.path.join(os.path.dirname(os.getcwd()), './data/market/tickerList.csv')

    handler = yahooData()
    tickers = pd.read_csv(tickerListPath)['Tickers']
    print(tickers)
    for ticker in tickers:
        try:
            print(ticker)
            df = handler.getDailyPrices(ticker, start='2018-01-01', end='2022-01-01')

            outname = '{}.csv'.format(ticker)
            outdir = './data/market'
            outdir = os.path.join(outdir, outname)
            fullname = os.path.join(os.path.dirname(os.getcwd()), outdir)

            df.to_csv(fullname)
        except:
            print("Couldn't download data for {}".format(ticker))

