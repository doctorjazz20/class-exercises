class classA:
    name='my name is class A'

if __name__ == '__main__':
    print('ATTRIBUTI DI CLASSE\n')

    print(classA.__dict__, '\n')

    #due istanze
    a1 = classA()
    a2 = classA()
    a1.name = 'sono stato rinominato'

    print('rinomina dell\' oggetto')
    print('classA.name=',classA.name)
    print('a1.name=',a1.name)
    print('a2.name=',a2.name)

    print('\n rinomina attributo di classe')
    classA.name= 'classe A rinominata'

    print('classA.name=', classA.name)
    print('a1.name=', a1.name)
    print('a2.name=', a2.name)

    print('\nattributi di classe e attributi d\'istanza')
    print('a1.__dict__=',a1.__dict__)
    print('a2.__dict__=',a2.__dict__)
    print('classA.__dict__=',classA.__dict__)