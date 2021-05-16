def calculate(number1, number2, operator):
    if number1 is None or number2 is None:
        return None
    if '+' in operator:
        return number1 + number2
    elif '-' in operator:
        return number1 - number2
    elif '/' in operator:
        return number1 / number2
    elif '*' in operator:
        return number1 * number2
    else:
        return "No valid operator!"