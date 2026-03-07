from brain_games.engine import game_engine
from brain_games.games.is_even import (
    MAX_TRIES,
    RULES,
    check_answer,
    get_question,
)


def main():
    game_engine(
        rules=RULES,
        max_tries=MAX_TRIES,
        func_question=get_question,
        check_answer=check_answer,
    )


if __name__ == "__main__":
    main()
