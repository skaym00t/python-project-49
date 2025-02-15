def calculate_question():
    import random

    gcd = []
    while len(gcd) < 2:
        gcd = []
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        if number_1 > number_2:
            smaller = number_2
        else:
            smaller = number_1
        for i in range(2, smaller + 1):
            if (number_1 % i == 0) and (number_2 % i == 0):
                gcd.append(i)
    return [number_1, number_2, gcd[-1]]


def result_game():
    from brain_games.games.game_3 import calculate_question

    print("Find the greatest common divisor of given numbers.")
    import prompt

    lose = 0
    correct_answer = ""
    user_answer = ""
    for i in range(3):
        number_1, number_2, correct_answer = calculate_question()
        print(f"Question: {number_1} {number_2}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
            continue
        else:
            lose += 1
            break
    return [lose, correct_answer, user_answer]
