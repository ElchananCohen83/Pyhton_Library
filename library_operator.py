from person import Person

class LibraryOperator(Person):

    def __init__(self, operator_last_name :str, operator_first_name :str, operator_password :str, operator_id :str=None):
        super().__init__(operator_last_name, operator_first_name, operator_id)
        self.__operator_password = operator_password

    @property
    def operator_password(self):
        return self.__operator_password

    @operator_password.setter
    def operator_password(self, new_password):
        self.__operator_password = new_password