# # class SingletonClass:
# #     _instance = None
# #
# #     def __init__(self, arg1, arg2):
# #         self.arg1 = arg1
# #         self.arg2 = arg2
# #
# #     def __new__(cls, *args, **kwargs):
# #         if not cls._instance:
# #             cls._instance = super().__new__(cls)
# #         return cls._instance
# #
# #
# # # Usage example
# # obj1 = SingletonClass("Hello", 123)
# # obj2 = SingletonClass("World", 456)
# #
# # print(obj1.arg1, obj1.arg2)  # Hello 123
# # print(obj2.arg1, obj2.arg2)  # Hello 123
# #
# # obj1.arg1 = "Modified"
# # obj2.arg2 = 789
# #
# # print(obj1.arg1, obj1.arg2)  # Modified 789
# # print(obj2.arg1, obj2.arg2)  # Modified 789
# # print(obj1 is obj2)  # True - Both variables refer to the same instance
# #
# # class A(SingletonClass):
# #
# #     def __init__(self, arg1, arg2, arg3):
# #         super.__init__(self, arg1, arg2)
# #         self.arg3 = arg3
# #
# #     def get_arg3(self):
# #         return self.arg3
# #
# #
# # a = A(1,2,3)
# # b = A(4,5,6)
# # print(a is b)
# # print(b.get_arg3())
# #
#
# class OnlyCreatable(object):
#
#     __create_key = object()
#
#     @classmethod
#     def create(cls, value):
#         if cls.__create_key == object():
#             cls.__create_key = OnlyCreatable(cls.__create_key, value)
#         return cls.__create_key
#
#     def __init__(self, create_key, value):
#         assert(create_key == OnlyCreatable.__create_key), \
#             "OnlyCreatable objects must be created using OnlyCreatable.create"
#         self.value = value
#
#     def get_value(self):
#         return self.value
#
#
# a = OnlyCreatable.create(1)
# b = OnlyCreatable.create(2)
#
# print(a is b)
# print(a.get_value())
#
# # class A(OnlyCreatable):
# #
# #     def __init__(self, arg1, arg2, arg3):
# #         super.__init__(self, arg1, arg2)
# #         self.arg3 = arg3
# #
# #     def get_arg3(self):
# #         return self.arg3
# #
# #
# # a = A(1,2,3)
# # b = A(4,5,6)
# # print(a is b)
#
#


class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._instance.__value = []
        return cls._instance

    def get_value(self):
        return self.__value

    def add(self, x):
        self.__value.append(x)


a = Logger.instance()
b = Logger.instance()
print(a is b)
print(a.get_value())
a.add(12)
print(a.get_value())
c = a.get_value()
c.append(13)
print(a.get_value())
class Logger2(Logger):
    pass

class MyClass():
    def __init__(self):
        self._my_list = [1, 2, 3, 4, 5]

    @property
    def my_list(self):
        return self._my_list.copy()

# Usage example
obj = MyClass()

print(obj.my_list)  # [1, 2, 3, 4, 5]

obj.my_list.append(6)  # Attempt to modify the list

print(obj.my_list)  # [1, 2, 3, 4, 5]


