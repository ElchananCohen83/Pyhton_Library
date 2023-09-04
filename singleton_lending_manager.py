from datetime import datetime, timedelta, date
from database import Database


class SingletonLendingManager():
    __lending_manager_instance = None


    def __new__(cls, *args, **kwargs):
        if cls.__lending_manager_instance is None:
            #Creating new instance
            cls.__lending_manager_instance = super().__new__(cls, *args, **kwargs)
            cls.__lending_manager_instance.__initialized = False
        return cls.__lending_manager_instance


    def __init__(self):
        if not self.__initialized:
            self.__lending_list = []
            self.__initialized = True
        else:
            raise RuntimeError('This class is of singelton type, and there is already one instance.')


    @property
    def lending_list(self):
        return self.__lending_list.copy()


    def select_lending_list(self):
        db = Database('library')
        rows = db.select('library')
        #Initialize instance
        self.__lending_list = []
        # Store the fetched data in a list
        for row in rows:
            self.__lending_list.append((row[0], row[1], row[2], row[3], row[4], row[5]))


    def add_lending_book(self, book_id, costumer_id):
        db = Database('library')

        # check if book in the exist
        if db.select_field_where('books', 'id', 'id' , book_id) == None:
            print('The book does not exist in the system')
            return

        # check if coustmer in the exist
        if db.select_field_where('costumers', 'id', 'id' , costumer_id) == None:
            print('The customer does not exist in the system')
            return

        # check if the book available
        available = db.select_field_where('books', 'available', 'id' , book_id)
        if available == '':
            # chack Some books already exist with the customer
            books_he_has = db.select_field_where('costumers', 'books_he_has', 'id' , costumer_id)
            if books_he_has < 3:
                # chack date_of_subscription
                date_of_subscription = datetime.strptime(db.select_field_where('costumers', 'date_of_subscription', 'id', costumer_id), '%Y-%m-%d')
                next_year = date_of_subscription + timedelta(days=365)
                if  next_year > datetime.now():
                    #insert row from table 'library'
                    db.insert_lending_book(book_id, costumer_id)
                    # update is book not available
                    library_id = db.select_field_where('library', 'id', 'book_id', book_id)
                    db.update('books', 'available', book_id, library_id )
                    # update Some books already exist with the customer
                    db.update('costumers', 'books_he_has', costumer_id, books_he_has + 1 )

                    self.select_lending_list()
                else:
                    print('Dear client! Your subscription has expired, you must renew your subscription.')
            else:
                print('Dear client! You already have 3 books on loan, it is not possible to borrow another book')
        else:
            print('book is not available')


    def return_lending(self, row_id):
        # Connect to the SQLite database
        db = Database('library')
        lending_id = db.select_field_where('library', 'id', 'id', row_id)
        if lending_id == None:
            print("The lending book does not exist")
            return
        lending_status = db.select_field_where('library', 'status', 'id', row_id)
        if lending_status == 0:
            print('The book has already been returned')
            return

        #update_status
        customer_id = db.select_field_where('library', 'customer_id', 'id', row_id)
        db.update('library', 'return_date', row_id , date.today() )
        db.update('library', 'status', row_id, '0')

        #update avalible in books table
        book_id = db.select_field_where('library', 'book_id', 'id', row_id )
        db.update('books', 'available', book_id, '')

        #update books_he_has in costumers table
        customer_id = db.select_field_where('library', 'customer_id', 'id', row_id)
        books_he_has = db.select_field_where('costumers', 'books_he_has', 'id', customer_id)
        db.update('costumers', 'books_he_has', customer_id, books_he_has-1 )

        self.select_lending_list()


    def customers_lending_book_search(self, book_name : str):
        for book in self.__book_list:
            if book_name == book.book_name:
                print(book.book_name, book.book_id)
                return
        print('The book does not exist')
        return


    def print_instance_lending(self):
        self.select_lending_list()
        for instance_library in self.__lending_list:
            print(f'lending_id: {instance_library[0]},   book_id: {instance_library[1]},   costumer_id: {instance_library[2]}, date_of_delivery: {instance_library[3]}, return_date: {instance_library[4]}, status: {instance_library[5]}')