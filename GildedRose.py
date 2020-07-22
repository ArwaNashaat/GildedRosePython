from abc import ABC, abstractmethod
import tkinter

class Quality(ABC):
    def __init__(self, qualityValue):
        self.qualityValue = qualityValue

    def setQualityValue(self, qualityValue):
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
        return
class Conjured_Quality(Quality):
    def updateQuality(self):
        self.qualityValue -= 2

        if self.qualityValue < 0:
            self.qualityValue = 0

class BackstagePasses_Quality(Quality):
    def updateQuality(self, sell_in):
        if sell_in <= 10 and sell_in > 5:
            self.qualityValue += 2
        elif sell_in <= 5 and sell_in >0:
            self.qualityValue += 3

        elif sell_in == 0:
            self.qualityValue = 0

        if self.qualityValue > 50:
            self.qualityValue = 50


class Item_AbstractBridge(ABC):
    @abstractmethod
    def __init__(self, name, sell_in, quality:Quality):
        pass
    def __repr__(self):
        return "%s, %s, %s" % ( self.sell_in, self.quality)

    @abstractmethod
    def isSellDatePassed(self):
        pass

class RegularItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:RegularQuality):
        self.name = "Regular"
        self.sell_in = sell_in
        self.__quality = quality

    def isSellDatePassed(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.__quality.updateQuality(2)
        else :
            self.__quality.updateQuality(1)

class AgedBrieItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:AgedBrie_Quality):
        self.name = "AgedBrie"
        self.sell_in = sell_in
        self.__quality = quality

    def isSellDatePassed(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.__quality.updateQuality(2)
        else:
            self.__quality.updateQuality(1)

class SulfurasItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:Sulfuras_Quality):
        self.name = "Sulfuras"
        self.sell_in = sell_in
        self.__quality = quality.setQualityValue(self,80)

    def isSellDatePassed(self):
        return

class BackstagePassesItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:BackstagePasses_Quality):
        self.name = "BackstagePasses"
        self.sell_in = sell_in
        self.__quality = quality

class ConjuredItem(Item_AbstractBridge):
    def __init__(self, name, sell_in, quality:Conjured_Quality):
        self.name = "Conjured"
        self.sell_in = sell_in
        self.__quality = quality

class ManageItems:

    def addItem(self, item:Item_AbstractBridge):
        file = Files()
        file.saveToFile(item)

class Files:
    def saveToFile(self, item:Item_AbstractBridge):
        f = open("articles.txt", "a")
        index = 0

        f.write(item.__name, item.__sell_in, item.__quality)
        index += 1
        f.close()


def main():


if __name__ == "__main__":
    main()
