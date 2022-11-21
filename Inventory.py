class Inventory():

    def __init__ (self, itemID, count, title, itemPrice):
        self.itemID = itemID
        self.count = count
        self.title = title
        self.itemPrice = itemPrice
    
    def getitemID(self):
        return self.itemID
        
    def getcount(self):
        return self.count
        
    def gettitle(self):
        return self.title
    def getitemPrice(self):
        return self.itemPrice
    
    def change_count(self, itemID, count):
        self.itemID = itemID
        self.count = count
        
    def __int__(self):
        return self.itemID + self.count
        
    def change_price(self, itemPrice, count):
        self.itemID = itemPrice
        self.newPrice = count
        
    def __int__(self):
        return itemPrice + count
        
    
