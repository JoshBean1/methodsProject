class Inventory:
    def __init__ (self, book_list, movie_list):
        self.book_list = book_list  # list of book class instances
        self.movie_list = movie_list  # list of movie class instances

    def view_books(self):
        for book in self.book_list:
            print(book)

    def view_movies(self):
        for movie in self.movie_list:
            print(movie)

    def view_all(self):
        print("Books:")
        self.view_books()
        print()

        print("Movies:")
        self.view_movies()
        print()

    def checkoutBook(self, ID):
        for book in self.book_list:
            if book.ID == ID:
                book.decrement()

    def checkoutMovie(self, ID):
        for movie in self.movie_list:
            if movie.ID == ID:
                movie.decrement()
