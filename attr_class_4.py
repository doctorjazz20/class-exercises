class fraction:

    @staticmethod
    def __gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    def __reduce(cls, num, den):
        gcd = cls.__gcd(num, den)
        return num // gcd, den // gcd

    def __init__(self, num, den):
        if num is None:
            raise Exception('num cannot be null')
        if den is None or den==0:
            raise Exception('denominator cannot be zero')
        self.__numerator, self.__denominator = fraction.__reduce(num, den)

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, num):
        if num is None:
            raise Exception('numerator cannot be null')
        self.__numerator, self.__denominator = fraction.__reduce(num, self.__denominator)

    @denominator.setter
    def denominator(self, den):
        if den is None or den==0:
            raise Exception('denominator cannot be zero')
        self.__numerator, self.__denominator = fraction.__reduce(self.__numerator, den)

    def __str__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)


if __name__ == '__main__':
    print('static method vs class method')
    q1 = fraction(6,4)
    print(q1)

    q1.denominator = 9
    print(q1)

    q1.numerator = 15
    print(q1)