class GetterSetter:
    __name = ''

    def __init__(self):
        print("I am init method")

    def __new__(cls):
        print("I am new method")
        return object.__new__(cls)

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, new_name):
        self.__name = new_name

    @get_name.deleter
    def get_name(self):
        del self.__name

    @classmethod
    def test(cls):
        cls.__name = ''

    def __del__(self):
        print("I am destroctor method")


obj = GetterSetter()
obj.get_name = 'hari'
print(obj.get_name)

del obj.get_name

print(obj.get_name)
