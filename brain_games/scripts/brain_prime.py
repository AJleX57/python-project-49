from brain_games.engine import run_game
from brain_games.games.prime import generate_prime_question


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(description, generate_prime_question)
    

if __name__ == "__main__":
    main()
