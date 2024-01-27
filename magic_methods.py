# def constant(val):
#
#     def valget(self):
#         return val
#
#     def valset(self, val):
#         raise AttributeError
#
#     return property(fget=valget, fset=valset)

class LocalTime:

    def __init__(self, hours, minutes, seconds):
        if not (hours >= 0 and minutes >= 0 and seconds >= 0):
            raise AttributeError('all parameters must be >0')
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, hours):
        self.__hours = hours

    @minutes.setter
    def minutes(self, minutes):
        self.__minutes = minutes

    @seconds.setter
    def seconds(self, seconds):
        self.__seconds = seconds

    def __add__(self, other):
        seconds = self.__seconds + other.seconds
        minutes = self.__minutes + other.minutes
        hours = self.__hours + other.hours
        if seconds >= 60:
            minutes += 1
            seconds -= 60
        if minutes >= 60:
            hours += 1
            minutes -= 60
        return LocalTime(hours=hours, minutes=minutes, seconds=seconds)

    def __str__(self):
        return f" {self.__hours}:{self.__minutes}:{self.__seconds}"


if __name__ == '__main__':
    print('MAGIC METHODS\n\n')

    time1 = LocalTime(10, 30, 45)
    time2 = LocalTime(5, 14, 35)

    print(f" time1={time1}")
    print(f" time2={time2}")

    print(f" time1+tme2={time1+time2}")