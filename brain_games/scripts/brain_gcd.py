from brain_games.engine import game_engine
from brain_games.games.gcd import MAX_TRIES, RULES, check_answer, find_gcd


def main():
    game_engine(
        rules=RULES,
        max_tries=MAX_TRIES,
        func_question=find_gcd,
        check_answer=check_answer,
    )


if __name__ == "__main__":
    main()
