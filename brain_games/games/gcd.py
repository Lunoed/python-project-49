from math import gcd
from random import randint

MAX_TRIES = 3
RULES = "Find the greatest common divisor of given numbers."


def find_gcd():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f"{num_1} {num_2}"
    answer = gcd(num_1, num_2)
    return question, answer


def check_answer(answer_1, answer_2):
    return str(answer_1) == str(answer_2)
