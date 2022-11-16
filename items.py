class items:
    def __init__(self, _name, _price, _barcode):
        self.price = _price
        self.name = _name
        self.barcode = _barcode

    def getprice(self):
        return self.price

    def getname(self):
        return self.name
    
    def getbarcode(self):
        return self.barcode
    
    def changeprice(self, newprice):
        self.price = newprice

    def changebarcode(self, newbarcode):
        self.barcode = newbarcode

    def changename(self, newname):
        self.name = newname
    
    def __str__(self):
        info = "Item name is", self.name,"/n Price is", self.price, "/n Barcode is", self.barcode,"/n"
        return info
