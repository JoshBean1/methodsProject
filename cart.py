class Item:
    def __init__(self, itemID, name, price, amnt, type):
        self.ID = itemID
        self.name = name
        self.price = price
        self.amnt = amnt
        self.type = type

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_amnt(self):
        return self.amnt

    def get_type(self):
        return self.type

    def set_ID(self, ID):
        self.ID = ID

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_amnt(self, amnt):
        self.amnt = amnt

    def add_amnt(self, amnt):
        self.amnt = (self.get_amnt() + amnt)

    def set_type(self, type):
        self.type = type


class Cart:
    # Define Cart as an object with a Cart ID and User ID
    # as well as a Dictionary containing a set of Items.
    def __init__(self, cartID, userID):
        self.ID = cartID
        self.userID = userID
        self.items = dict()

    # Adds an item to the current cart
    # Returns a 0 if the item was added and there were no duplicates
    # Returns a 1 if there was a duplicate item present, and the item's amount was changed
    # Returns a -1 on error (Item not added to list)
    def add_item(self, item):
        # Check if cart is empty
        if (not (self.items)):
            self.items.update({item.get_ID():item})
        # Check new item's ID against other items currently in the cart
        for i in self.items:
            # If the new item's ID doesn't match the current checked item's ID, continue
            if i != item.get_ID():
                continue
            # If the new Item's ID matches the current checked item's ID, add the new item's Amount to the checked item's Amount
            # and follow with a Return so the function completes
            elif i == item.get_ID():
                self.items[i].add_amnt(item.amnt)
                return 1
            # If all items have been checked and no items' IDs match the new item's ID, add the new item to the end of the list
            if i == (self.items.len() - 1):
                self.items.update({item.get_ID(): item})
                return 0
        return -1

    # Gets the total number of items in the cart
    def get_num_items(self):
        total_items = 0
        for i in self.items:
            total_items = total_items + self.items[i].get_amnt()
        return total_items

    # Removes an item from the cart based on its position in the Cart List
    def remove_item_index(self, item_key):
        self.items.pop(item_key)

    # Removes an item from the cart based on its Item ID
    def remove_item_ID(self, item_ID):
        self.items.pop(item_ID)
        return

    # Clears all items from the cart, returns the number of items removed upon completion
    def remove_all_items(self):
        num_removed = 0
        for i in self.items:
            num_removed = num_removed + self.items[i].get_amnt()
            self.items.pop(i)
        return num_removed

    # Gets and returns the total price of all items within the cart at once
    def get_total_price(self):
        total = 0
        for i in self.items:
            total = total + self.items[i].get_price()
        return total




item1 = Item(1, "Book1", 10., 1, "Book")
item2 = Item(2, "Movie1", 9., 2, "Movie")
item3 = Item(3, "Book2", 8., 1, "Book")
item4 = Item(1, "Book1", 10., 2, "Book")

cart = Cart(100, 10000)

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)
cart.add_item(item4)

print("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total_price()))
cart.remove_item_ID(1)
print("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total_price()))
