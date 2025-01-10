def result_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    import prompt
    import random

    lose = 0
    correct_answer = ""
    user_answer = ""
    for i in range(3):
        number = random.randint(0, 100)
        if number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        user_answer = answer
        if user_answer == correct_answer:
            print("Correct!")
            continue
        else:
            lose += 1
            break
    return [lose, correct_answer, user_answer]
