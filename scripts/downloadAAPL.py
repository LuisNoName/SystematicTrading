import Packages.DataHandler
from Packages.DataHandler.yahooData import yahooData
import pandas as pd
import os

if __name__ == '__main__':
    handler = yahooData()
    df_aapl = handler.getDailyPrices('AAPL', start='2010-01-01', end='2022-01-01')

    outname = 'AAPL.csv'

    outdir = './data/market'
    outdir = os.path.join(outdir, outname)
    fullname = os.path.join(os.path.dirname(os.getcwd()), outdir)

    df_aapl.to_csv(fullname)