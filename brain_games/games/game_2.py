def result_game():
    print("What is the result of the expression?.")
    import prompt
    import random

    lose = 0
    correct_answer = ""
    user_answer = ""
    for i in range(3):
        number_1 = random.randint(1, 50)
        number_2 = random.randint(1, 15)
        operators = ["+", "-", "*"]
        operator = random.choice(operators)
        if operator == "+":
            correct_answer = number_1 + number_2
        elif operator == "-":
            correct_answer = number_1 - number_2
        else:
            correct_answer = number_1 * number_2
        print(f"Question: {number_1} {operator} {number_2}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
            continue
        else:
            lose += 1
            break
    return [lose, correct_answer, user_answer]
