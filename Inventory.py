class Inventory():

    def __init__ (self, itemID, count, itemType, title, itemPrice):
        self.itemID = itemID
        self.count = count
        self.itemType = itemType
        self.title = title
        self.itemPrice = itemPrice
   
    def change_count(self, itemID, count):
       self.itemID = itemID
       self.count = count
       return self.itemID + self.count
    def change_price(self, itemPrice, count):
        self.itemPrice = itemPrice
        self.count = count
        return self.itemPrice + self.count
        
    def veiew_all_items():
        
