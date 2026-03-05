from brain_games.games.gcd import MAX_TRIES, RULES, find_gcd, check_answer
from brain_games.engine import game_engine

def main():
    game_engine(
        rules=RULES,
        max_tries=MAX_TRIES,
        func_question=find_gcd,
        check_answer=check_answer
    )


if __name__ == '__main__':
    main()
