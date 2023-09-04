class Person:
    def __init__(self, last_name, first_name, id):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__id = id

    @property
    def id(self):
        return self.__id

    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def full_name(self):
        return self.__first_name + ' ' + self.__last_name
