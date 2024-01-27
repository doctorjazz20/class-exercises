# class B(object):
#     def __init__(self):
#         print("B.__init__")
#         super().__init__()
#
#
# class C(object):
#     def __init__(self):
#         print("C.__init__")
#         super().__init__()
#
#
# class D(C, B):
#     def __init__(self):
#         print("D.__init__")
#         super().__init__()

class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()


class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

# errore Cannot create a consistent method resolution
# order (MRO) for bases A, C

# class E(A, C):
#     def __init__(self):
#         print("E.__init__")
#         super().__init__()


if __name__ == '__main__':
    # e = E()
    # print('\n')
    d = D()
    print('\n')
    c = C()
    print('\n')
    b = B()
    print('\n')
    a = A()
