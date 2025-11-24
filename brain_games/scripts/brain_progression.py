from brain_games.engine import run_game
from brain_games.games.progression import generate_progression_question


def main():
    description = "What number is missing in the progression?"
    run_game(description, generate_progression_question)


if __name__ == "__main__":
    main()
