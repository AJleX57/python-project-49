import random


def calculate_expression(num1, num2, operator):
    """Вычисляет результат выражения"""
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError(f"Unknown operator: {operator}")


def generate_calc_question():
    """Генерирует вопрос и правильный ответ для калькулятора"""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate_expression(num1, num2, operator))
    
    return question, correct_answer
