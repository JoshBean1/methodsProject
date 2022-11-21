import csv

class Cart:
    def __init__(self, ID, userID, itemID, itemCount):
        self.ID = ID
        self.userID = userID
        self.itemID = itemID
        self.itemCount = itemCount
        self._update()

    def view_cart(self):
        # Function allows all contents of cart to be displayed
        return

    def remove_item(self, item, count):
        # Function removes an item from the cart (by ID), one at a time (maybe change so that it takes in a "Count" to remove, or -1 to remove all)
        self._update()

    def add_item(self, item, count):
        # Function adds an amount of an item (by ID) to cart
        self._update()

    def get_total(self):
        # Function returns the total cost of all items in cart to user
        return

    def _update(self):
        # Update contents of cart
        return