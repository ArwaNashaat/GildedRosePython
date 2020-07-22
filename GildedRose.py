from abc import ABC
import mysql.connector

class GildedRose(object):

    def __init__(self, items):
        self.items = items

class Item_AbstractBridge(ABC):
    def __init__(self, sell_in, quality: QualityInterface):
        self.__sell_in = sell_in
        self.__quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class RegularItem(Item_AbstractBridge):
class AgedBrieItem(Item_AbstractBridge):
class SulfurasItem(Item_AbstractBridge):
class BackstagePassesItem(Item_AbstractBridge):
class ConjuredItem(Item_AbstractBridge):

class ManageDataBase:
    def createDataBase(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="arwa",
            password=""
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE mydatabase")

def main():
    managedataBase=ManageDataBase()
    managedataBase.createDataBase()


if __name__ == "__main__":
    main()
