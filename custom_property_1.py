class verbose_property:

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.__fget = fget
        self.__fset = fset
        self.__fdel = fdel

        print("\n__init__ called with:)")
        print(f"fget={fget}, fset={fset}, fdel={fdel}, doc={doc}")

        if doc is None and fget is not None:
            self.__doc__ = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        print(f"\n__get__ called with obj={obj}, objtype={objtype}")
        if obj is None:
            return self
        if self.__fget is None:
            raise AttributeError("unreadable attribute")
        return self.__fget(obj)

    def __set__(self, obj, value):
        if self.__fset is None:
            raise AttributeError("can't set attribute")
        self.__fset(obj, value)

    def __delete__(self, obj):
        if self.__fdel is None:
            raise AttributeError("can't delete attribute")
        self.__fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.__fset, self.__fdel, self.__doc__)

    def setter(self, fset):
        print(type(self))
        return type(self)(self.__fget, fset, self.__fdel, self.__doc__)

    def deleter(self, fdel):
       return type(self)(self.__fget, self.__fset, fdel, self.__doc__)

class car:

    def __init__(self, targa=None, anno_matricola=None):
        self.__targa=targa
        self.__anno_matricola=anno_matricola

    @verbose_property
    def targa(self):
        return self.__targa

    #stesso effetto annotazione
    #targa = verbose_property(fget=targa, fset=None, fdel= None, doc = '')

    @targa.setter
    def targa(self, targa = None):
        self.__targa = targa

if __name__ == '__main__':
    print('CUSTOM PROPERTY DEMO!!!')

    car = car('ABC123')
    car.targa = 'XX'
    print(car.targa)