from abc import ABC, abstractmethod

class DataHandler(ABC):

    def __init__(self):
        if type(self) is DataHandler:
            raise Exception('Base is an abstract class and cannot be instantiated directly')

    @abstractmethod
    def getDailyPrices(self):
        pass