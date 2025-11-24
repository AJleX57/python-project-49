from brain_games.engine import run_game
from brain_games.games.calc import generate_calc_question


def main():
    description = "What is the result of the expression?"
    run_game(description, generate_calc_question)


if __name__ == "__main__":
    main()
