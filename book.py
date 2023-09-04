from  genre import Genre

class Book:

    def __init__(self, book_name :str, author_name :str, genre :Genre, age_restriction :bool, publishing_year :int=0,  number_of_pages: int=0, available: str='', book_id = None):
        self.__book_name = book_name
        self.__author_name = author_name
        self.__genre = genre
        self.__publishing_year = publishing_year
        self.__age_restriction = age_restriction
        self.__number_of_pages = number_of_pages
        self.__available = available
        self.__book_id = book_id

    @property
    def book_id(self) ->str:
        return self.__book_id

    @property
    def book_name(self) ->str:
        return self.__book_name

    @property
    def author_name(self)->str:
        return self.__author_name

    @property
    def genre(self)->Genre:
        return self.__genre

    @property
    def publishing_year(self)->int:
        return self.__publishing_year

    @property
    def age_restriction(self)->bool:
        return self.__age_restriction

    @property
    def number_of_pages(self)->int:
        return self.__number_of_pages

    @property
    def available(self)->bool:
        return self.__available

    @property
    def __str__(self):
        return f'id: {self.__book_id}, book_name: {self.__book_name},  author_name: {self.__author_name}, genre: {self.genre}, publishing_year: {self.publishing_year}, number_of_pages: {self.number_of_pages}, age_restriction: {self.age_restriction} , available: {self.available}'