from logging import raiseExceptions
from shop import shop
from cart import cart
from os import system
import time

class till:
    def __init__(self):
        self.newshop = shop("lidl")
        self.newcart = cart()
        self.receiptnum = 0

    def runner(self):
        end = False
        print("**Welcome to Herts Supermarket Checkout System**")
        while end is False:
            option = None
            incorrect = False
            while (option != "1") and (option != "0"):
                if incorrect:
                    print("Invalid[!]. ", end="")
                option = input("Scan barcode [0] or exit [1]: ")
                incorrect = True
            option = int(option)
            if (option == 0):
                codeentry = True
                while codeentry:
                    newbarcode = self.getbarcode() 
                    self.addtocart(newbarcode)
                    codeentry = self.checkbarcodeentry(newbarcode)
                if self.newcart.checkempty():
                    print("Exiting with empty cart")
                    time.sleep(2)
                    system('cls')
                    notempty = False
                else:
                    list, total =  self.displaycart()
                    notempty = True
                    asktopay = self.paychoice()
                    while (asktopay == False) and (notempty == True):
                        _codeentry = True
                        if self.choiceremove():
                            removing = self.checkremoveitem()
                            while removing:
                                item = self.newcart.popitem()
                                print("You removed", item.getname(), end=".\n")
                                if not self.newcart.checkempty():
                                    removing = self.checkremoveitem()
                                else:
                                    removing = False 
                            if not self.newcart.checkempty():
                                list, total =  self.displaycart()
                                asktopay = self.paychoice()
                            else:
                                print("Exiting with empty bag")
                                notempty = False
                        else:
                            while _codeentry:
                                newbarcode = self.getbarcode() 
                                self.addtocart(newbarcode)
                                _codeentry = self.checkbarcodeentry(newbarcode)
                            list, total =  self.displaycart()
                            asktopay = self.paychoice()
                    if notempty:
                        change = self.paying(total)
                        receiptchoice = input("All paid. Would you like a receipt [y]/[n]: ")
                        self.printreceipt(receiptchoice, list, change, total)
                    time.sleep(1)
                    system('cls')
                    self.newcart.emptycart()
                    
                print("**Thank you for shopping with us**")
                time.sleep(3)
                system('cls')
                print("**Welcome to Herts Supermarket Checkout System**")
            if (option == 1):
                print("**System Exit**")
                time.sleep(3)
                system('cls')
                end = True

    def displaycart(self):
        time.sleep(2)
        system('cls')
        print ("-----------Scanned Items------------")
        _list = (self.newcart.showcart())
        for line in _list:
            print (line)
        _total = self.newcart.getcost()
        print("\nYour total amount is £", end="")
        print("{:.2f}".format(_total), end="\n\n")
        return _list, _total

    def checkremoveitem(self):
        invalid = False
        choice = ""
        while (choice != "y") and (choice != "n"):
            if invalid:
                print("Invalid[!]. ", end="")
            choice = input("Remove last added item? [y][n]: ")
            invalid = True
        if choice == "y":
            return True
        else: return False

    def printreceipt(self, _receiptchoice, _list, _change, _total):
        error = True
        while error == True:
            if (_receiptchoice == 'y'):
                error = False
                __change = "{:.2f}".format(_change)
                __total = "{:.2f}".format(_total)
                self.receiptnum += 1
                num = str(self.receiptnum)
                with open('C:\\Users\\Chukwudi\\Desktop\\receipt'+num+'.txt', 'w') as f:
                    f.write("------------------Receipt-----------------\n")
                    for line in _list:
                        f.write(line)
                        f.write("\n\n")
                    f.write(f"Change: £{__total} \n")
                    f.write(f"Total: £{__change} \n")
            elif (_receiptchoice == 'n'):
                error = False
            else:
                _receiptchoice = input("[!].Would you like a receipt [y]/[n]: ")

    def addtocart(self, _newbarcode):
        if self.checkfalseentry(_newbarcode, self.newshop):  #checks if barcode entry is valid
            print("Invalid entry[!]. ", end="")
        elif self.checkbarcodeentry(_newbarcode):            #if it is valid and not "y", get the item and add to cart
            newitem = self.newshop.getitem(_newbarcode) 
            self.newcart.addtocart(newitem)

    def removefromcart(self, _newbarcode):
        if self.checkfalseentry(_newbarcode, self.newshop):  #checks if barcode entry is valid
            print("Invalid entry[!]. ", end="")
        elif self.checkbarcodeentry(_newbarcode):            #if it is valid and not "y", get the item and add to cart
            self.newcart.removeitem(_newbarcode)
                
    def getbarcode(self):
        barcode = input("Please enter product barcode. Key in (y) to stop: ")
        return barcode
    
    def checkbarcodeentry(self, _barcodeentry):
        if (_barcodeentry == "y"):
            return False
        else: return True

    def checkfalseentry(self, _barcode, _shop):
        if _barcode != "y":
            if _shop.getitem(_barcode) == 1:
                return True
        else: return False
    #-----------------------    
    def payment(self, _total, _paid):
        _unpaid, _change = 0, 0
        if (_total > _paid):
            _unpaid = _total - _paid
            _change = 0
            return _unpaid, _change
        else:
            _change = _paid - _total
            _unpaid = 0
            return _unpaid, _change

    def paychoice(self):
        invalid = False
        choice = ""
        while (choice != "1") and (choice != "0"):
            if invalid:
                print("Invalid[!]. ", end="")
            choice = input("Press [0] to continue to payment or [1] to edit cart: ")
            invalid = True
        choice = int(choice)
        if choice == 1:
            return False
        else: return True

    def choiceremove(self):
        invalid = False
        choice = "q"
        while (choice != "1") and (choice != "0"):
            if invalid:
                print("Invalid[!]. ", end="")
            choice = input("Press [0] to remove, [1] to add: ")
            invalid = True
        if choice == "1":
            return False
        else: return True

    def paying(self, _total):
        paid = input("Enter amount paid: ")
        paid = int(paid)
        unpaid , change = self.payment(_total, paid)
        unpaidstr, changestr = "{:.2f}".format(unpaid), "{:.2f}".format(change)
        while (unpaid != 0):
            print(f"Total amount left is £{unpaidstr}")
            paid = input("Enter amount paid: ")
            paid = int(paid)
            unpaid , change = self.payment(unpaid, paid)
            unpaidstr, changestr = "{:.2f}".format(unpaid), "{:.2f}".format(change)
        if (change > 0):
            print("Your change is £{:.2f}".format(change))
        return change


        
    
newtill = till()
newtill.runner()