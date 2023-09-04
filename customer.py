from person import Person
from datetime import date


class Customer(Person):

    def __init__(self, customer_last_name, customer_first_name, customer_id = None, customer_date_of_subscription=date.today(), customer_books_he_has=0):
        super().__init__(customer_last_name, customer_first_name, customer_id)
        self.__customer_date_of_subscription = customer_date_of_subscription
        self.__customer_books_he_has = customer_books_he_has

    @property
    def customer_date_of_subscription(self):
        return self.__customer_date_of_subscription


    @customer_date_of_subscription.setter
    def customer_date_of_subscription(self, new_date):
        self.__customer_date_of_subscription = new_date

    @property
    def customer_books_he_has(self):
        return self.__customer_books_he_has

    @property
    def __str__(self):
        return f'id: {self.id}, last_name: {self.last_name}, first_name: {self.first_name},  date_of_subscription: {self.__customer_date_of_subscription}, books_he_has: {self.__customer_books_he_has}'