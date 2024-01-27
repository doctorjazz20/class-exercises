class Q:

    def __init__(self, numerator, denominator):

        if denominator is None or denominator==0:
            raise AttributeError('denominator must be not null and not zero')

        (self.__numerator, self.__denominator) = Q.__reduce(numerator, denominator)

    def __str__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    @staticmethod
    def __gcd(n1, n2):
        while n2!=0:
            (n1, n2)=(n2, n1 % n2)
        return n1

    @classmethod
    def __reduce(cls, numerator, denominator):
        gcd = cls.__gcd(numerator, denominator)
        return (numerator//gcd, denominator//gcd)

if __name__ == '__main__':
    q1 = Q(26,10)
    print(q1)

    q2 = Q(40,10)
    print(q2)

    q3 = Q(7, 10)
    print(q3)