from database import Database
from singleton_lending_manager import SingletonLendingManager
from datetime import date
from random import randint
from singleton_books_manager import SingletonBooksManager
from book import Book

db = Database('library')
#db.update('costumers', 'date_of_subscription', 5, date.today())

db1 = Database('library')
#print(db1.select_field_where('costumers', 'books_he_has', 'id', 1))

#library = SingletonLendingManager()
#library.add_lending_book(12, 101)
#for i in range(1248):
#db1.update('costumers', 'books_he_has', 28, 0)
#db1.update('costumers', 'books_he_has', 3, 0)
#db1.select_field_where('books', 'available', 'id', 12)
#db1.delete('library', 1)
#print(db1.select_field_where('library', '"costumer_id", "book_id", "date_of_delivery", "return_date"', 'status', 1))
import sqlite3
con = sqlite3.connect('library.db')
cursor = con.cursor()
cursor.execute('SELECT * FROM library WHERE status=1')
con.commit()
rows = cursor.fetchall()
print(rows)

#select_where_query = f"SELECT {column} FROM {table_name} WHERE {row} = {value}"
#cursor = self.execute(select_where_query)
#print(db1.select_field_where('library', '*', 'status', 1))