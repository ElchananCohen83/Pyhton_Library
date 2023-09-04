from singleton_books_manager import SingletonBooksManager
from singleton_customer_manager import SingletonCustomersManager
from singleton_lending_manager import SingletonLendingManager
from library_operator import LibraryOperator
from database import Database

class LibraryManager:

    def __init__(self):
        self.__books_manager = SingletonBooksManager()
        self.__customers_manager = SingletonCustomersManager()
        self.__lending_manager = SingletonLendingManager()

    @property
    def books_manager(self):
        return self.__books_manager

    @property
    def customer_manager(self):
        return self.__customers_manager

    @property
    def lending_manager(self):
        return self.__lending_manager

    """    @property
    def librarian(self):
        return self.__librarian"""

    def select_active_lending_details(self):
        db = Database('library')
        active_lending_details = db.select_field_where('library', ' "id" , "book_id", "costumer_id", "date_of_delivery", "return_date" ', 'status', 1)
        #print(active_lending_details)

        active_lending_details_dict = {}
        for lending in active_lending_details:
            customer_full_name = db.select_field_where('costumers', ' "costumer_last_name", "costumer_first_name" ','id', lending[2])
            customer_full_name = f'{lending[2]}: {customer_full_name[0][0]} {customer_full_name[0][1]}'
            book_name = db.select_field_where('books', 'book_name', 'id', lending[1])
            if customer_full_name not in active_lending_details_dict:
                #active_lending_details_dict[customer_full_name] = [f'{book_name} .id:{lending[1]}']
                active_lending_details_dict[customer_full_name] = [book_name, lending[1]]

            else:
                active_lending_details_dict[customer_full_name].append(book_name)
                active_lending_details_dict[customer_full_name].append(lending[1])
        for key, value in active_lending_details_dict.items():
            print(key)
            for i in range(0,len(value)-1,2):
                print(f'book_id:{value[i+1]}, book_name: {value[i]}')
            print()