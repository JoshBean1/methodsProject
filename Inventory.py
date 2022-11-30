class Inventory:
    def __init__ (self, book_list, movie_list):
        self.book_list = book_list  # list of book class instances
        self.movie_list = movie_list  # list of movie class instances


    def __str__(self): #view all items
        return str(self.book_list) + str(self.movie_list)

    def inc_count(self):
        self.quantity += 1
    def dec_count(self):
        self.quantity -= 1
        
    def view_books(self):
        f = open("books.txt")
        book_content = f.read()
        print(book_content)
        f.close()
    def view_movies(self):
        f =open("movies.txt")
        movie_content = f.read()
        print(movie_content)
        f.close()
