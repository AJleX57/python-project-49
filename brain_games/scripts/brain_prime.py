from brain_games.engine import run_game
from brain_games.games.prime import generate_prime_question


def main():
    description = 'What is the result of the expression?'
    run_game(description, generate_prime_question)
    

if __name__ == "__main__":
    main()
