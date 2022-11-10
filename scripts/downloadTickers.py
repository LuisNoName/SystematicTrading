from Packages.DataHandler.yahooData import yahooData
import pandas as pd
import os
from datetime import date

if __name__ == '__main__':
    tickerListPath = os.path.join(os.path.dirname(os.getcwd()), './data/market/tickerList.csv')

    handler = yahooData()
    tickers = pd.read_csv(tickerListPath)['Tickers']
    for ticker in tickers:
        try:
            print("Downloading price data for {}".format(ticker))
            df = handler.getDailyPrices(ticker, start = '2000-01-01', end = date.today())

            outname = '{}.csv'.format(ticker)
            outdir = './data/market'
            outdir = os.path.join(outdir, outname)
            fullname = os.path.join(os.path.dirname(os.getcwd()), outdir)

            df.to_csv(fullname)
        except:
            print("Couldn't download data for {}".format(ticker))

    print("Data download finished.")
