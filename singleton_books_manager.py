from book import Book
from database import Database

class SingletonBooksManager:
    __library_manager_instance = None


    def __new__(cls, *args, **kwargs):
        if cls.__library_manager_instance is None:
            #Creating new instance
            cls.__library_manager_instance = super().__new__(cls, *args, **kwargs)
            cls.__library_manager_instance.__initialized = False
        return cls.__library_manager_instance


    def __init__(self):
        if not self.__initialized:
            self.__book_list = []
            self.__initialized = True
        else:
            raise RuntimeError('This class is of singelton type, and there is already one instance.')


    @property
    def book_list(self):
        return self.__book_list.copy()

    def select_books_list(self):
        db = Database('library')
        rows = db.select('books')
        #Initialize instance
        self.__book_list = []
        # Store the fetched data in a list
        for row in rows:
            self.__book_list.append(Book(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0]))


    def add_book(self, book_instance: Book):
        import sqlite3
        # Connect to the SQLite database
        conn = sqlite3.connect('library.db')
        # Create a cursor object
        cursor = conn.cursor()
        books_data = [(book_instance.book_name, book_instance.author_name, book_instance.genre, book_instance.publishing_year, book_instance.age_restriction, book_instance.number_of_pages, book_instance.available), ]
        cursor.executemany(
            "INSERT INTO books (book_name, author_name, genre, publishing_year, age_restriction, number_of_pages, available) VALUES(?, ?, ?, ?, ?, ?, ?)",books_data)
        conn.commit()  # Remember to commit the transaction after executing INSERT.

        self.select_books_list()


    def delete_row_in_books(self, row_id: int):
        # Connect to the SQLite database
        db = Database('library')
        if db.select_field_where('library', 'book_id', 'id', row_id) == None:
            #delete_row
            db.delete('books', row_id)
            self.select_books_list()
        else:
            print('The book cannot be removed, the book is currently on loan to a customer')


    def get_catalog_books(self):
        # Connect to the SQLite database
        db = Database('library')
        rows = db.catalog('books', 'book_name')
        counter = 0
        for row in rows:
            counter += 1
            print(*row, f'.{counter}')

    def book_search(self, book_name : str):
        self.select_books_list()

        for book in self.__book_list:
            if book_name == book.book_name:
                print(f'id: {book.book_id}, book_name: {book.book_name}')
                return
        print('The book does not exist')
        return

    def print_instance_book(self):
        self.select_books_list()
        for instance_book in self.__book_list:
            print(instance_book.__str__)