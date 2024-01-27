# esercizio 1 overriding metodi custom
class Person:

    def __new__(cls, *args, **kwargs):
        print('new Person called')
        return super().__new__(cls)

    def __init__(self, name=None, surname=None):
        print('init Person called')
        self.name = name
        self.surname = surname
        super().__init__()

    def __str__(self):
        return 'Person[]'

    def saluta(self):
        print('ciao')


# esercizio 2 estensione
class Employee(Person):

    def __new__(cls, *args, **kwargs):
        print('new Employee called')
        return super().__new__(cls)

    def __init__(self, name=None, surname=None):
        super().__init__(name, surname)

    # senza il super l'override è automatico
    def saluta(self):
        super().saluta()
        print('hello!!')


class Team:
    name = 'security'
    building = 'first palace'

    @staticmethod
    def static_saluta():
        print('hello static team')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # esercizio 1
    print('ESERCIZIO 1\n\n')

    p1 = Person()
    print(str(p1))
    print(p1.saluta(), Person.saluta(p1))
    print(p1.__getattribute__('name'))

    p2 = Person('mario')
    print(p2.__getattribute__('name'))
    print(p2.__getattribute__('surname'))

    try:
        print(p2.__getattribute__('nonexistent'))
    except Exception as e:
        print(e.__repr__())

    ## esercizio 2
    print('\n\nESERCIZIO 2\n\n')

    e1 = Employee('alberto')
    print(e1.__getattribute__('name'))

    # restituisce i parametri di istanza
    print(e1.__dict__)
    # restituisce i metodi i magic e le ineritanze
    print(Employee.__dict__)

    print('\n\n')

    e1.saluta()
    # Employee.saluta() non va bene
    Employee.saluta(e1)

    print('\n STATIC PARAMETERS\n')

    t = Team()
    Team.static_saluta()
    print(Team.__dict__)
    print(t.__dict__)
