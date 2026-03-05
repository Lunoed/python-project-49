from random import choice


MAX_TRIES = 3
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer(num: int, answer: str) -> bool:
    return (num % 2 == 0 and answer.lower().strip() == "yes") or (
        num % 2 != 0 and answer.lower().strip() == "no"
    )


def get_question():
    nums = [num for num in range(1, 101)]
    num = choice(nums)
    print(f"Question: {num}.")
    answer = "yes" if num % 2 == 0 else "no"
    return num, answer
