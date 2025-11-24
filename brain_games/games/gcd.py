from math import gcd
from random import randint

from brain_games.games.welcome import hello


def b_gcd():
    name = hello()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        print(F'Question: {num_1} {num_2}')
        answer = int(input('Your answer: '))
        result = gcd(num_1, num_2)
        if answer == result:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}.'")
            print(f'Lets try again, {name}.')
            break
    if count == 3:
        print(f'Congratulations, {name}.')
