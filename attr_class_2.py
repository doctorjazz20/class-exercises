class Car:

    #attr. classe
    # tiene il n. di istanze della classe
    __counter = 0

    #costruttore
    def __init__(self, plate=None, build_year=None):
        type(self).__counter += 1
        self.plate=plate
        self.build_year=build_year

    def __del__(self):
        type(self).__counter -= 1

    @staticmethod
    def CarInstances():
        return Car.__counter

if __name__=='__main__':
    print('ATTR. DI CLASSE 2\n')

    print('Car.counter=',Car.CarInstances())
    car1 = Car('ABC123', 1980)
    print('car1.__dict__=', car1.__dict__)
    print('Car.counter=', car1.CarInstances())
    car2 = Car('ABC124', 1982)
    print('Car.counter=', car2.CarInstances())
    del car1
    print('Car.counter=', Car.CarInstances())
    del car2
    print('Car.counter=', Car.CarInstances())

    car3 = Car()
    print('car3.__dict__=', car3.__dict__)