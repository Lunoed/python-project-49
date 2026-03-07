from brain_games.engine import game_engine
from brain_games.games.is_prime import (
    MAX_TRIES,
    RULES,
    check_answer,
    get_question,
)


def main():
    game_engine(
        rules=RULES,
        max_tries=MAX_TRIES,
        check_answer=check_answer,
        func_question=get_question,
    )


if __name__ == "__main__":
    main()
