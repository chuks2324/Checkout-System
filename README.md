# Checkout-System
This code is an implementation of a supermarket checkout system using python with a focus on Object Oriented Programming. The code is split into four files one of which is the main code which runs the checkout system.

## The Files
- #### Cart.py
This defines the cart class which contains an array which stores items selected by the customer via the barcode.
It also includes methods to remove all items, remove the last item added to the array.
- #### Items.py
This class method defines object properties of each item in the supermarket. This properties are the _price_, _item name_ and _barcode_. Get methods have been defined to return each object property and change each property.
A string method also returns a detailed information about the item object.
The constructor method takes in all three properties as input.
- #### Shop.py
The shop class has two object properties. They are:
- An array _items_ which stores the item objects in the shop.
- The _shopname_. 

The constructor method takes in a shopname as input.
The _items_ array has been populated with dummy items at the constructor method with the following item obejcts

|   Item name    |    Price  | Barcode  |
| -------------- | ----------| -------- |
|       Milk     |   10.50   |  0120001 |
|     Bread      |   5.50    | 0120002  |
|    Chocolate   |   8.00    |  0120003 |
|      Towel     |   12.10   |  0120004 |
|   Toothpaste   |   6.75    |  0120005 |
|      Soap      |   5.20    | 0120006  |
|       Pen      |   2.00    |  0120007 |
|     Biscuits   |   4.45    |  0120008 |
|       Lamp     |   20.50   |  0120009 |
|     Battery    |   10.00   |  0120010 |

- #### Runner.py
All aforementioned classes are imported into this file.
Specific functions to help the running of the code are defined and called on at different time using the code logic.

