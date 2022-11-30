class Inventory:

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
        
    def view_all_items(self):
        import os
        files = [] #['movies' 'books']
        merged_data = ""

        while True:
            f_name = input("Enter the file name: ")
            files.append(f_name)
            ans = input("Want to view another file?(y/n): ").lower()
            if ans!='y':
                break
        for file in files:
            filename = file + '.txt'
            if os.path.isfile(filename):
                f = open(filename, mode='r', encoding='utf-8')
                merged_data = merged_data + f.read()
                f.close() 
        f.write(merged_data)
        print("See all items in new list")

