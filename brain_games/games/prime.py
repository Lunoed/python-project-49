from random import randint

from .welcome import hello


def prime(number):
    num = number // 2
    k = 2 
    while k <= num:
        if number % k == 0:
            return 'no'
        else:
            k += 1
    else:
        return 'yes'


def is_prime():
    name = hello()
    print('Answer "yes" if given number is prime. ' 
          'Otherwise answer "no".')
    count = 0
    while count < 3:
        num = randint(1, 50)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        res = prime(num)
        if answer == res:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' was wrong answer ;(. "
                  f"Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
