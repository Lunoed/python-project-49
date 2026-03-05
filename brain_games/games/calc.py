from random import choice, randint


MAX_TRIES = 3
RULES = "What is a result of the expression?"


def get_question():
    num_1 = randint(0, 100)
    num_2 = randint(0, 100)
    num_3 = randint(0, 10)
    operations = ("+", "-", "*")
    operator = choice(operations)
    question = f"{num_1} {operator} {num_3 if operator == '*' else num_2}"
    print(f"Question: {question}.")
    answer = int(eval(question))
    return str(eval(question)), answer


def check_answer(question: str, answer: str | int) -> bool:
    return question == answer
