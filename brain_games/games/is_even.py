from random import choice

MAX_TRIES = 3
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer(correct_answer: str, answer: str) -> bool:
    return correct_answer == answer.lower().strip()


def get_question():
    nums = [num for num in range(1, 101)]
    num = choice(nums)
    print(f"Question: {num}.")
    answer = "yes" if num % 2 == 0 else "no"
    return answer
