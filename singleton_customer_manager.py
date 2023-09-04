from customer import Customer
from database import Database
from datetime import date
import sqlite3

class SingletonCustomersManager:
    __customer_manager_instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__customer_manager_instance is None:
            #Creating new instance
            cls.__customer_manager_instance = super().__new__(cls, *args, **kwargs)
            cls.__customer_manager_instance.__initialized = False
        return cls.__customer_manager_instance

    def __init__(self):
        if not self.__initialized:
            self.__customers_list = []
            self.__initialized = True
        else:
            raise RuntimeError('This class is of singelton type, and there is already one instance.')

    @property
    def customers_list(self):
        return self.__customers_list.copy()

    def select_customers_list(self):
        db = Database('library')
        rows = db.select('costumers')
        #Initialize instance
        self.__customers_list = []
        # Store the fetched data in a list
        for row in rows:
            self.__customers_list.append(Customer(row[2], row[1], row[0], row[3], row[4]))

    def add_customers(self, customers_instance: Customer):
        # Connect to the SQLite database
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        costumer_data = [(customers_instance.last_name, customers_instance.first_name, customers_instance.customer_date_of_subscription, customers_instance.customer_books_he_has), ]
        cursor.executemany(
            "INSERT INTO costumers (costumer_last_name, costumer_first_name, date_of_subscription, books_he_has) VALUES(?, ?, ?, ?)",costumer_data)
        conn.commit()  # Remember to commit the transaction after executing INSERT.

        self.select_customers_list()


    def delete_customers(self, customer_id: int):
        # Connect to the SQLite database
        db = Database('library')
        if db.select_field_where('library', 'costumer_id', 'costumer_id', customer_id) == None:
            # delete_row
            db.delete('costumers', customer_id)
            self.select_customers_list()
        else:
            print('The customer cannot be removed, The customer has a book')


    def date_of_subscription(self, customers_id):
        db = Database('library')
        db.update('costumers', 'date_of_subscription', customers_id, date.today())

        self.select_customers_list()


    def customers_search(self, customers_name : str):
        self.select_customers_list()
        for customers in self.__customers_list:
            if customers_name == customers.full_name:
                print(f'{customers.full_name} ,id:{customers.id}')
                return
        print('The customers does not exist')
        return

    def print_instance_customers(self):
        self.select_customers_list()
        for instance_customer in self.__customers_list:
            print(instance_customer.__str__)