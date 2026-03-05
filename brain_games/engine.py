import prompt
from typing import Callable
from brain_games.cli import welcome_user


def game_engine(
    rules: str, max_tries: int, func_question: Callable, check_answer: Callable
):
    name = welcome_user()
    print(rules)
    count = 0
    while count < max_tries:
        quest, correct_answer = func_question()
        answer = prompt.string("Your answer: ")
        check = check_answer(quest, answer)
        if check:
            print("Correct!")
            count += 1
        else:
            print(f"{answer} is wrong answer ;( Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    engine()
