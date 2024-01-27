class Foo:

    def __init__(self, value=None):
        self.__value = value

    @property
    def attribute1(self):
        print(f'returning attribute for instance = {self}')
        return self.__value

    @attribute1.setter
    def attribute1(self, value):
        print(f'setting attribute={value} for instance = {self}')
        self.__value = value


if __name__ == '__main__':
    my_foo_object = Foo(42)
    print(my_foo_object)
    print(my_foo_object.attribute1)

    my_foo_object.attribute1 = 51
    print(my_foo_object)
    print(my_foo_object.attribute1)