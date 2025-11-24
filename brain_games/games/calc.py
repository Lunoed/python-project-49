from random import randint, shuffle

from .welcome import hello


def ress():
    a = randint(1, 100)
    b = randint(1, 100)
    ress = a + b
    print(f'Question: {a} + {b}')
    answer = int(input('Your answer: '))
    if answer == a + b:
        print('Correct!')
    else:
        print(f'{answer} is wrong naswer ;(.Correct answer was {ress})')
        print(f"Lets's try again, {name}!")
        raise SystemExit(0)
        

def minus():
    a = randint(1, 100)
    b = randint(1, 100)
    ress = a - b
    print(f'Question: {a} - {b}')
    answer = int(input('Your answer: '))
    if answer == a - b:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong naswer ;(. "
              f"Correct answer was '{ress})'.")
        print(f"Lets's try again, {name}!")
        raise SystemExit(0)
        

def multiplication():
    a = randint(1, 10)
    b = randint(1, 10)
    ress = a * b
    print(f'Question: {a} * {b}')
    answer = int(input('Your answer: '))
    if answer == a * b:
        print('Correct!')
    else:
        print(f'{answer} is wrong naswer ;(.Correct answer was {ress})')
        print(f"Lets's try again, {name}!")
        raise SystemExit(0)


def calc():
    global name
    name = hello()
    functions = [multiplication, minus, ress]
    shuffle(functions)
    for func in functions:
        func()
    print(f'Congratulations, {name}!')
