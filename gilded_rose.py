from abc import ABC, abstractmethod
import tkinter
from doctest import master


class Quality(ABC):
    def __init__(self, qualityValue:int):
        self.qualityValue = qualityValue

    def setQualityValue(self, qualityValue:int):
        self.qualityValue = qualityValue

    @abstractmethod
    def updateQuality(self):
        pass



class RegularQuality(Quality):
    def __init__(self, qualityValue):
        self.qualityValue = qualityValue

    def updateQuality(self, decreasingValue):
        self.qualityValue -= decreasingValue

        if self.qualityValue < 0:
            self.qualityValue = 0


class AgedBrie_Quality(Quality):
    def updateQuality(self, increasingValue:int):
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
    def updateQuality(self, sell_in:int):
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
    def __init__(self, name, sell_in:int, quality:Quality):
        pass
    #def __repr__(self):
        #return "%s, %s, %s" % (self.name, self.sell_in, self.quality.qualityValue)

    @abstractmethod
    def isSellDatePassed(self):
        pass
    def getName(self):
        return self.name
    def getSellin(self):
        return self.sell_in

    def getQuality(self):
        return self.quality.qualityValue

class RegularItem(Item_AbstractBridge):
    def __init__(self, name, sell_in:int, quality):
        self.name = "Regular"
        self.sell_in = int(sell_in)
        self.quality = RegularQuality(quality)

    def isSellDatePassed(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.getQuality().updateQuality(2)
        else :
            self.getQuality().updateQuality(1)

class AgedBrieItem(Item_AbstractBridge):
    def __init__(self, name, sell_in:int, quality:AgedBrie_Quality):
        self.name = "AgedBrie"
        self.sell_in = sell_in
        self.quality = quality

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
        self.quality = quality.setQualityValue(80)

    def isSellDatePassed(self):
        return

class BackstagePassesItem(Item_AbstractBridge):
    def __init__(self, name, sell_in:int, quality:BackstagePasses_Quality):
        self.name = "BackstagePasses"
        self.sell_in = sell_in
        self.quality = quality

class ConjuredItem(Item_AbstractBridge):
    def __init__(self, name, sell_in:int, quality:Conjured_Quality):
        self.name = "Conjured"
        self.sell_in = sell_in
        self.quality = quality


def getItemName(window, variable):

    item_name = tkinter.OptionMenu(master, variable, "Regular Item", "Aged Brie", "Sulfuras",
                                   "BackstagePasses", "Conjured")
    item_name.grid(row = 0)

def getItemQuality_Sell_in(window, itemNameParam, itemList):
    sell_in_var = tkinter.IntVar()
    qualityValue_var = tkinter.IntVar()
    def submit():
        sell_in = sellin_entry.get()
        qualityValue = qualityValue_var.get()
        itemName = itemNameParam.get()

        if itemName == "Regular Item":
            item = RegularItem(itemName, sell_in,RegularQuality(qualityValue))
        elif itemName == "Aged Brie":
            item = AgedBrieItem(itemName, sell_in,AgedBrie_Quality(qualityValue))
        elif itemName == "Sulfuras":
            item = SulfurasItem(itemName, sell_in,Sulfuras_Quality(qualityValue))
        elif itemName == "BackstagePasses":
            item = BackstagePassesItem(itemName, sell_in,BackstagePassesItem(qualityValue))
        else:
            item = ConjuredItem(itemName, sell_in,Conjured_Quality(qualityValue))
        itemList.append(item)

    sellin_label = tkinter.Label(window, text='Sell In')

    sellin_entry = tkinter.Entry(window,
                          textvariable=sell_in_var)

    qualityValue_label = tkinter.Label(window,
                           text='Quality Value')


    qualityValue_entry = tkinter.Entry(window,
                           textvariable=qualityValue_var)

    sub_btn = tkinter.Button(window, text='add item',
                        command=submit)

    sellin_label.grid(row=3, column=0)
    sellin_entry.grid(row=3, column=1)
    qualityValue_label.grid(row=4, column=0)
    qualityValue_entry.grid(row=4, column=1)
    sub_btn.grid(row=5, column=1)

def updateSellIn(window, itemList):
    def iterateOverItemList():
        print(len(itemList))
        for i in itemList:
            i.isSellDatePassed()
            print(i.getQuality)
    sub_btn = tkinter.Button(window, text='update sell in',
                             command= iterateOverItemList)

    sub_btn.grid(row=6, column=1)

def main():
    itemList = []
    window = tkinter.Tk()
    window.title("GUI")
    window.geometry("312x324")

    variable = tkinter.StringVar(master)
    variable.set("Regular Item")

    getItemName(window, variable)
    getItemQuality_Sell_in(window, variable, itemList)

    updateSellIn(window, itemList)
    window.mainloop()


if __name__ == "__main__":
    main()
