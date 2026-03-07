from random import randint

MAX_TRIES = 3
RULES = "What number in missing in the progression?"
PROG_LEN = 10


def get_question() -> tuple[str, str]:
    progression, answer = make_progression()
    question = progression
    return question, answer


def check_answer(correct_answer: str, user_responce: str) -> bool:
    return user_responce == correct_answer


def make_progression() -> tuple[str, str]:
    first_num = randint(1, 100)
    step = randint(1, 20)
    progression = []
    count = 0
    while len(progression) < PROG_LEN:
        progression.append(str(first_num + step * count))
        count += 1
    index = randint(0, 9)
    hidden_num = progression[index]
    progression[index] = ".."
    str_progression = " ".join(progression)
    return str_progression, hidden_num
