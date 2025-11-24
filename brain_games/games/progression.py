import random


def generate_arithmetic_progression(start, step, length):
    """Генерирует арифметическую прогрессию"""
    return [start + i * step for i in range(length)]


def generate_progression_question():
    """Генерация вопроса и ответа для прогрессии"""
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    progression = generate_arithmetic_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)

    progression_with_hidden = progression.copy()
    correct_answer = str(progression_with_hidden[hidden_index])
    progression_with_hidden[hidden_index] = ".."

    question = " ".join(map(str, progression_with_hidden))

    return question, correct_answer
