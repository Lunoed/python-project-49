from .welcome import hello
from random import randint


def progression():
    name = hello()
    count = 0
    while count < 3:
        step = randint(1, 20)
        idnx = randint(0, 9)
        x_num = randint(1, 30)
        nums = []
        for i in range(1, 11):
            nums.append(x_num + i * step)
        numbers = nums.copy()
        numbers[idnx] = '..'
        print('What number is missing in the progression?')
        print(f'Question: {numbers}')
        answer = int(input('Your answer: '))
        if answer == nums[numbers.index('..')]:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' was wrong answer ;(."
                f"Correct answer was '{nums[numbers.index('..')]})'")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
