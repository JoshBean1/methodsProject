from movieandbook import *

class Cart:
    # Define Cart as an object with a Cart ID and User ID
    # as well as two lists containing individual sets of Books and Movies, respectively.
    def __init__(self, cartID, userID):
        self.ID = cartID
        self.userID = userID
        self.books = []
        self.movies = []


    def add_book(self, book): # Attempts to add a book to the Books list.
        keyCount = 0          # Returns 0 if book was appended to end of list, 1 if the book was already in the list (count will be updated), and -1 on error.
        numBooks = len(self.books)
        if (numBooks == 0):
            self.books.append(book)
            return 0
        for bookKey in self.books:
            if self.books[keyCount].ID == book.ID: # Book duplicate ID found in list, add to the Count of the found book and return 1
                self.books[keyCount].count = self.books[keyCount].count + book.count
                return 1
            else: # No duplicate ID found in Books list, continue search until end of list found
                keyCount = keyCount + 1
                if (keyCount >= len(self.books)): # If the end of the list is found, then add the new book to the end of the list and return 0
                    self.books.append(book)
                    return 0
                else:
                    continue
        return -1


    def add_movie(self, movie): # Attempts to add a movie to the Movies list.
        keyCount = 0            # Returns 0 if movie was appended to end of list, 1 if the movie was already in the list (count will be updated), and -1 on error.
        numMovies = len(self.movies)
        if (numMovies == 0):
            self.movies.append(movie)
            return 0
        for movieKey in self.movies:
            if self.movies[keyCount].ID == movie.ID: # Movie duplicate ID found in list, add to the Count of the found movie and return 1
                self.movies[keyCount].count = self.movies[keyCount].count + movie.count
                return 1
            else: # No duplicate ID found in Movies list, continue search until end of list found
                keyCount = keyCount + 1
                if (keyCount >= len(self.movies)): # If the end of the list is found, then add the new movie to the end of the list and return 0
                    self.movies.append(movie)
                    return 0
                else:
                    continue
        return -1


    def get_num_items(self): # Gets the total number of items in the cart
        total_items = 0
        for item in self.books:
            total_items = total_items + item.count
        for item in self.movies:
            total_items = total_items + item.count
        return total_items


    def remove_book_index(self, item_key): # Removes a book from the cart based on its position in the Cart's Book List
        self.books.pop(item_key)
        return

    
    def remove_movie_index(self, item_key): # Removes a movie from the cart based on its position in the Cart's Movie List
        self.movie.pop(item_key)
        return

    
    def remove_item_ID(self, item_ID): # Removes an item from the cart based on its Item ID
        for item in self.books:
            if (item.ID == item_ID):
                self.books.remove(item)
        for item in self.movies:
            if (item.ID == item_ID):
                self.movies.remove(item)
        return

    
    def remove_all_items(self): # Clears all items from the cart, returns the number of items removed upon completion
        total_num_removed = self.get_num_items()
        self.books.clear()
        self.movies.clear()
        return total_num_removed

    
    def get_total_price(self): # Gets and returns the total price of all items within the cart at once
        price = 0
        for item in self.books:
            price = price + (int(item.price)) * item.count
        for item in self.movies:
            price = price + (int(item.price)) * item.count
        return price


    def print_items_and_price(self): # Prints out an easy-to-view statistic of the number of items in and total price of the cart
        print("You have %i items in your cart for a total of $%.02f" % (self.get_num_items(), self.get_total_price()))
        return

    
    def view_books(self): # Prints out each Book within the list formatted as follows: - ID, Name, Count, Price
        for book in self.books:
            print(" - ISBN: ", book.ID, ", Title: \"", book.name, "\", Count: ", book.count, ", Cost: $%.02f" % int(book.price), "\n", end = '', sep = '')
        return


    def view_movies(self): # Prints out each Movie within the list formatted as follows: - ID, Name, Count, Price
        for movie in self.movies:
            print(" - ISBN: ", movie.ID, ", Title: \"", movie.name, "\", Count: ", movie.count, ", Cost: $%.02f" % int(movie.price), "\n", end = '', sep = '')
        return


    def view_cart(self): # Prints out each item within the list.
        print("Books: ")
        self.view_books()
        print("\nMovies: ")
        self.view_movies()
        return
