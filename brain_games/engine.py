from typing import Callable

import prompt

from brain_games.cli import welcome_user


def game_engine(
    rules: str, max_tries: int, func_question: Callable, check_answer: Callable
):
    name = welcome_user()
    print(rules)
    count = 0
    while count < max_tries:
        question, correct_answer = func_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        check = check_answer(correct_answer, answer)
        if check:
            print("Correct!")
            count += 1
        else:
            print(f"{answer} is wrong answer ;( ", end="")
            print(f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")
