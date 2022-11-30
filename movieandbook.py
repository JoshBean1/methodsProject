import csv

class Book:
    def __init__(self, ID, name, count, price):
        self.ID = ID
        self.name = name
        self.count = int(count)
        self.price = price

    def __str__(self):
        return self.ID + '. ' + self.name + ' -> $' + self.price + ' (' + str(self.count) + ' left in stock) '

    def increment(self):
        self.count += 1
        self._update()

    def decrement(self):
        self.count -= 1
        if self.count == 0:
            self.delete_book()
            return
        self._update()

    def delete_book(self):
        lines = []  # store csv in memory

        with open('books.txt', 'r') as books_file:
            books_read = csv.reader(books_file, delimiter=',')
            for row in books_read:
                if self.ID != row[0]:  # read all books into list except for current book
                    lines.append(row)
        with open('books.txt', 'w') as books_file:  # overwrite books.txt file with updated data
            books_write = csv.writer(books_file, delimiter=',')
            books_write.writerows(lines)  # old unchanged books

    def _update(self):  # write class to csv file
        lines = []  # store csv in memory
        current_book = [self.ID, self.name, str(self.count), self.price]

        with open('books.txt', 'r') as books_file:
            books_read = csv.reader(books_file, delimiter=',')
            for row in books_read:
                if self.ID != row[0]:  # read all books into list except for current book
                    lines.append(row)
        with open('books.txt', 'w') as books_file:  # overwrite books.csv file with updated data
            books_write = csv.writer(books_file, delimiter=',')
            books_write.writerows(lines)  # old unchanged books
            books_write.writerow(current_book)  # new book


class Movie:
    def __init__(self, ID, name, count, price):
        self.ID = ID
        self.name = name
        self.count = int(count)
        self.price = price

    def __str__(self):
        return self.ID + '. ' + self.name + ' -> $' + self.price + ' (' + str(self.count) + ' left in stock) '

    def increment(self):
        self.count += 1
        self._update()

    def decrement(self):
        self.count -= 1
        if self.count == 0:
            self.delete_movie()
            return
        self._update()

    def delete_movie(self):
        lines = []  # store csv in memory

        with open('movies.txt', 'r') as movies_file:
            movies_read = csv.reader(movies_file, delimiter=',')
            for row in movies_read:
                if self.ID != row[0]:  # read all movies into list except for current movie
                    lines.append(row)
        with open('movies.txt', 'w') as movies_file:  # overwrite movies.txt file with updated data
            movies_write = csv.writer(movies_file, delimiter=',')
            movies_write.writerows(lines)  # old unchanged movies

    def _update(self):  # write class to csv file
        lines = []  # store csv in memory
        current_movie = [self.ID, self.name, str(self.count), self.price]

        with open('movies.txt', 'r') as movies_file:
            movies_read = csv.reader(movies_file, delimiter=',')
            for row in movies_read:
                if self.ID != row[0]:  # read all movies into list except for current movie
                    lines.append(row)
        with open('movies.txt', 'w') as movies_file:  # overwrite movies.csv file with updated data
            movies_write = csv.writer(movies_file, delimiter=',')
            movies_write.writerows(lines)  # old unchanged movies
            movies_write.writerow(current_movie)  # new movie
