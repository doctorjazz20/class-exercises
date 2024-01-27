class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(B, C):
    pass


if __name__ == '__main__':
    x = D()
    x.m()

    print(D.mro())

    # ho forzato la scelta della classe
    print('\n SCELTA FORZATA\n')

    A.m(x)
    B.m(x)
    C.m(x)
