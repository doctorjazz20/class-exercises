class Wrapper:

    def __init__(self, value=None):
        self.__value = value

    def __set__(self, instance, value):
        print(f'setting value={value} for instance={instance} and self={self}')
        self.__value = value

    def __get__(self, instance, owner):
        print(f'getting value from instance={instance} and owner={owner}')
        return self.__value


class Foo:
    attribute1 = Wrapper(None)


if __name__ == '__main__':
    my_foo_object = Foo()
    print(my_foo_object)

    x = my_foo_object.attribute1
    print(x)

    my_foo_object.attribute1 = Wrapper(42)
    print(my_foo_object.attribute1)
