class Genre():
    action1 = 'action'
    def __init__(self):
        self.__actiom = 'actiom'
        self.__tension = 'tension'
        self.__horror = 'horror'
        self.__comedy = 'comedy'
        self.__drama = 'drama'
        self.__israeli = 'israeli'
        self.__classic = 'classic'
        self.__children = 'children'
        self.__documentary = 'documentary'

    @property
    def action(self)->str:
        return self.__actiom

    @property
    def tension(self)->str:
        return self.__tension

    @property
    def horror(self)->str:
        return self.__horror

    @property
    def comedy(self)->str:
        return self.__comedy

    @property
    def drama(self)->str:
        return self.__drama

    @property
    def israeli(self)->str:
        return self.__israeli

    @property
    def classic(self)->str:
        return self.__classic

    @property
    def children(self)->str:
        return self.__children

    @property
    def documentary(self)->str:
        return self.__documentary



# class Gener:
#     Action = 'action'
#     Tension = 'tension'
#     Horror = 'horror'
#     Comedy = 'comedy'
#     Drama = 'drama'
#     Israeli = 'israeli'
#     Classic = 'classic'
#     Children = 'children'
#     Documentary = 'documentary'
#
#     @staticmethod
#     def get_action():
#         return Gener(Gener.Action)
#
#     @staticmethod
#     def get_tension():
#         return Gener(Gener.Tension)
#
#     @staticmethod
#     def get_horror():
#         return Gener(Gener.Horror)
#
#     @staticmethod
#     def get_drama():
#         return Gener(Gener.Drama)
#
#     @staticmethod
#     def get_israeli():
#         return Gener(Gener.Israeli)
#
#     @staticmethod
#     def get_action():
#         return Gener(Gener.Classic)
#
#     @staticmethod
#     def get_action():
#         return Gener(Gener.Children)
#
#     @staticmethod
#     def get_action():
#         return Gener(Gener.Documentary)
#
#
#     def __init__(self, gener = 'action'):
#         self.__gener = gener
#
#     def get_gener(self):
#         return self.__gener
#
# Gener2.get_action()