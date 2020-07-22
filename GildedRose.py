from abc import ABC, abstractmethod
from datetime import datetime

import mysql.connector

'''
class GildedRose(object):

    def __init__(self, items):
        self.items = items


class Quality(ABC):
    @abstractmethod
    def updateQuality(self, sell_in):
        pass


class RegularQuality(Quality):
    def updateQuality(self, sell_in):
        


class Item_AbstractBridge(ABC):
    def __init__(self, sell_in, quality: Quality):
        self.__sell_in = sell_in
        self.__quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class RegularItem(Item_AbstractBridge):
class AgedBrieItem(Item_AbstractBridge):
class SulfurasItem(Item_AbstractBridge):
class BackstagePassesItem(Item_AbstractBridge):
class ConjuredItem(Item_AbstractBridge):
'''
class Quality(ABC):
    def __init__(self, qualityValue):
        self.qualityValue = qualityValue

    @abstractmethod
    def updateQuality(self):
        pass
    @abstractmethod
    def sellDatePassed(self):
        pass


class RegularQuality(Quality):
    def updateQuality(self, decreasingValue):
        self.qualityValue -= decreasingValue

        if self.qualityValue < 0:
            self.qualityValue = 0


class AgedBrie_Quality(Quality):
    def updateQuality(self, increasingValue):
        self.qualityValue += increasingValue
        if self.qualityValue > 50:
            self.qualityValue = 50

class Sulfuras_Quality(Quality):
    def updateQuality(self):
        self.qualityValue = 80

class Conjured_Quality(Quality):
    def updateQuality(self):
        self.qualityValue -= 2

        if self.qualityValue < 0:
            self.qualityValue = 0

class BackstagePasses_Quality(Quality):
    def updateQuality(self, sell_in):
        if sell_in <= 10 and sell_in > 5:
            self.qualityValue += 2
        elif sell_in <= 5:
            self.qualityValue += 3

        if self.qualityValue > 50:
            self.qualityValue = 50


class Item_AbstractBridge(ABC):

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abstractmethod
    def isSellDatePassed(self):
        pass

class RegularItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:RegularQuality):
        self.name = name
        self.sell_in = sell_in
        self.__quality = quality

    def isSellDatePassed(self):
        current_time = datetime.datetime.now()
        if self.sell_in > current_time.day:
            self.__quality.updateQuality(2)

class AgedBrieItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:AgedBrie_Quality):
        self.name = name
        self.sell_in = sell_in
        self.__quality = quality

    def isSellDatePassed(self):
        current_time = datetime.datetime.now()
        if self.sell_in > current_time.day:
            self.__quality.updateQuality(2)

class SulfurasItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:Sulfuras_Quality):
        self.name = name
        self.sell_in = sell_in
        self.__quality = quality

    def isSellDatePassed(self):
        print("do nothing") #temprory

class BackstagePassesItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:BackstagePasses_Quality):
        self.name = name
        self.sell_in = sell_in
        self.__quality = quality

class ConjuredItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:Conjured_Quality):
        self.name = name
        self.sell_in = sell_in
        self.__quality = quality

'''        
class ManageDataBase:
    def createDataBase(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="arwa",
            password=""
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE mydatabase")
'''
def main():
    '''managedataBase=ManageDataBase()
    managedataBase.createDataBase()
    '''

if __name__ == "__main__":
    main()
