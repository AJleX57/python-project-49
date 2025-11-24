import prompt


def run_game(game_description, generate_question_answer):
    """
    Общий движок для всех игр
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_description)

    rounds_count = 3

    for _ in range(rounds_count):
        question, correct_answer = generate_question_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
