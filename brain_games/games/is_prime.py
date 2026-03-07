from random import randint

RULES = 'Answer "yes" if number us prime. Otherwise answer "no".'
MAX_TRIES = 3


def is_prime(num: int) -> bool:
    num = num
    answer = True
    denominators = [i for i in range(2, num // 2 + 1)]
    for number in denominators:
        if num % number == 0:
            answer = False
    return answer


def get_question():
    rand_num = randint(1, 100)
    answer = is_prime(rand_num)
    correct_answer = "yes" if answer else "no"
    return rand_num, correct_answer


def check_answer(correct_answer: str, answer: str) -> bool:
    return answer == correct_answer
