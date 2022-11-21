class Book():
    def _init_(self, ID, name, count, price):
        self.ID = ID
        self.name = name
        self.count = count
        self.price = price

    def add_book_to_cart(self, ISBN, name, count, price):
        self.ID = ID
        self.name = name
        self.count = count
        self.price = price
        return self.ID
        return self.name
        return self.count
        return self.price


class Movie():
    def _init_(self, ID, name, count, price):
        self.ID = ID
        self.name = name
        self.count = count
        self.price = price

    def add_movie_to_cart(self, ISBN, name, count, price):
        self.ID = ID
        self.name = name
        self.count = count
        self.price = price
        return self.ID
        return self.name
        return self.count
        return self.price


f = open("myCart.txt", "a")

ID = input("Enter an ID: ")
f.write("{" + ID + ",  ")
name = input("Enter an name: ")
f.write(name + ",   ")
count = input("Enter a count: ")
f.write(count + ",   ")
price = input("Enter a price: ")
f.write(price + "}" + "\n")

f.close()
