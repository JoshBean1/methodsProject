class Inventory:
    def __init__ (self, quantity):
        self.quantity = quantity
        self.book_list = []
        self.movie_list = []
    
    def inc_count(self):
       self.count += 1
    def dec_count(self):
        self.count -= 1
        
    def __repr__(self): #veiw all items
        return str(self.book_list) + str(self.movie_list)
        
    def veiw_books(self):
        f = open("book.txt")
        book_content = f.read()
        print(book_content)
        f.close()
    def veiw_movies(self):
        f =open("movie.txt")
        movie_content = f.read()
        print(movie_content)
        f.close()
