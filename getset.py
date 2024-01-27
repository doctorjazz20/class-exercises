class Car:

    def __init__(self, plate=None, power=None):
        self.__plate = plate
        self.__power = power

    @property
    def plate(self):
        return self.__plate

    @plate.setter
    def plate(self, plate):
        self.__plate = plate


# decorator getter e setter




if __name__ == '__main__':
    print('GETTERS AND SETTERS\n')

    c1 = Car()
    c1.plate = 'ABC123'
    print(c1.plate)
