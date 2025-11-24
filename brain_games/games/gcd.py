import math
import random


def generate_gcd_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer
