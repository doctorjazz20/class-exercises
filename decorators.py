# decoratore
def art_deco(fun):
    def wrapper():
        print('before function called')
        fun()
        print('after function called')

    return wrapper


class art_deco_2:

    def __init__(self, fun1, fun2=None):
        self.__fun1 = fun1
        self.__fun2 = fun2

        print("\n__init__ called with:")
        print(f"fun1 = {fun1}, fun2={fun2}")

    def __get__(self, obj, objtype=None):
        print(f"\n__get__ called with obj={obj}, objtype={objtype}")
        if obj is None:
            return self
        if self.__fun1 is None:
            raise AttributeError("unreadable attribute")
        return self.__fun1(obj)


if __name__ == '__main__':
    print('DECORATORE 1\n\n')


    @art_deco
    def saluta():
        print('saluto')

    saluta()

    print('\n')

    def saluta2():
        print('saluto2')

    art_deco(saluta2).__call__()

    print('\n')

    @art_deco_2
    def saluta3():
        print('saluto2')

    saluta3()

