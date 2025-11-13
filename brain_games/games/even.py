from random import randint

from brain_games.games.welcome import hello


def even():
    name = hello()
    print('Answer "yes" if the number is even, '
    'otherwise answer "no".')
    count = 0
    while count < 3:
        num = randint(1, 100)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        if (num % 2 == 0 and answer == 'yes') \
            or (num % 2 != 0 and answer == 'no'):
            print('Correct!')
            count += 1
        else:
            result = 'yes' if answer == 'no' else 'no'
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}'.")
            break
    if count == 3:
        print(f'Congratulations, {name}')
