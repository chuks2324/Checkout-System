from items import items
from shop import shop
class cart:
    def __init__(self):
        self.bag = []

    def addtocart(self, _item):
        self.bag.append(_item)

    def popitem(self):
        item = self.bag.pop()
        return item
            

    def showcart(self):
        receipt = []
        listindex = 0
        for x in self.bag:
            poundprice = "{:.2f}".format(x.getprice())
            xprice = "£"+str(poundprice)
            receipt.append(f"{listindex+1}     {x.getbarcode()}     {xprice}      {x.getname()}")
            listindex += 1
        return receipt

    def emptycart(self):
        self.bag = []
    
    def getcost(self):
        total = 0
        for item in self.bag:
            total += item.getprice()
        return total
    def checkempty(self):
        if self.bag:
            return False
        else: return True

