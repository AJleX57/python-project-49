from brain_games.engine import run_game
from brain_games.games.gcd import generate_gcd_question


def main():
    description = "Find the greatest common divisor of given numbers."
    run_game(description, generate_gcd_question)


if __name__ == "__main__":
    main()
