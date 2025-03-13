def adu(a, b):
    return a+b


def scadu(a, b):
    return a-b


def multu(a, b):
    return a*b


def impartu(a, b):
    return round(a/b, 2)


operations = {
    '+': adu,
    '-': scadu,
    '*': multu,
    '/': impartu
}
print("Calculator v13.7")
while True:
    numar1 = input('Introduceti primul numar: ')
    if not numar1.isdigit():
        print('Introduceti un numar!')
        continue
    numar1 = int(numar1)
    break

calc = True
while calc:
    operator = input('Alegeti operatia  + , - , * , / sau C pentru a sterge: ')
    if operator not in ['+', '-', '*', '/', 'C', 'c']:
        print('Va rugam alegeti din nou!')
        pass
    elif operator == 'C' or operator == 'c':
        numar1 = input('Introduceti primul numar: ')
        if not numar1.isdigit():
            print('Introduceti un numar!')
            continue
        numar1 = int(numar1)
        break
    elif operator in ['+', '-', '*', '/']:
        numar2 = input('Introduceti urmatorul numar: ')
        if not numar2.isdigit():
            print('Introduceti un numar!')
            continue
        else:
            numar2 = int(numar2)
        if numar2 == 0 and operator == '/':
            print('Impartirea nu se poate face.')
            pass
        else:
            calculator = operations[operator]
            solutie = calculator(numar1, numar2)
            print(f'{numar1} {operator} {numar2} = {solutie}')
            numar1 = solutie
    else:
        break
