from items import items


class shop:
    def __init__(self, _shopname):
        self.items = []
        self.items.append(items("Milk", 10.50, "0120001"))
        self.items.append(items("Bread", 5.50, "0120002"))
        self.items.append(items("Chocolate", 8.00, "0120003"))
        self.items.append(items("Towel", 12.10, "0120004"))
        self.items.append(items("Toothpaste", 6.75, "0120005"))
        self.items.append(items("Soap", 5.20, "0120006"))
        self.items.append(items("Pen", 2.00, "0120007"))
        self.items.append(items("Biscuits", 4.45, "0120008"))
        self.items.append(items("lamp", 20.50, "0120009"))
        self.items.append(items("Battery", 10.00, "0120010"))
        self.shopname = _shopname

    def additem (self, _items):
        self.items.append(_items)

    def getitem(self, _barcode):
        for item in self.items:
            if _barcode == item.getbarcode():
                return item
        return 1

    def getshopname(self):
        return self.shopname