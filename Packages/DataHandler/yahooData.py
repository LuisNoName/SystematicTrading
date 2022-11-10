import pandas_datareader.yahoo.daily as yahoo

from Packages.DataHandler.DataHandler import DataHandler


class yahooData(DataHandler):

    def __init__(self, idx=2801):
        super().__init__()
        self.id = 2801

    def getDailyPrices(self, symbols=None, start=None, end=None, retry_count=3,
                       pause=0.1, session=None, adjust_price=False, ret_index=False,
                       chunksize=1, interval='d', get_actions=False, adjust_dividends=True):
        df = yahoo.YahooDailyReader(symbols=symbols, start=start, end=end, retry_count=retry_count,
                                    pause=pause, session=session, adjust_price=adjust_price, ret_index=ret_index,
                                    chunksize=chunksize, interval=interval, get_actions=get_actions,
                                    adjust_dividends=adjust_dividends)
        ret = df.read()
        df.close()
        return ret
