class VerboseWrapper:

    def __init__(self, v=None):
        self.__v = v

    def __get__(self, instance, owner):
        print(f" accessing value for instance = {instance} owner={owner}")
        return self.__v

    def __set__(self, instance, value):
        print(f" setting value for instance={instance}, value={value}")
        self.__v = value

    def __str__(self):
        return " VerboseWrapper=" + str(self.__v)


class Foo:
    attribute2 = VerboseWrapper('My Value!!')

    def __init__(self, attribute):
        self.attribute = attribute


if __name__ == '__main__':
    x = Foo(VerboseWrapper('My Value!!'))
    print(x.attribute)
    print(x.attribute2)

    x2 = Foo(VerboseWrapper('My Value!!'))
    x2.attribute2 = VerboseWrapper('Updated!!!')
    print(x2.attribute2)
    print(x.attribute2)
