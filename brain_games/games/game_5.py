def result_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    import prompt
    import random
    lose = 0
    correct_answer = ''
    user_answer = ''
    for i in range(3):
        number_1 = random.randint(1, 100)
        if number_1 == 1:
            correct_answer = 'no'
        elif number_1 == 2 or number_1 == 3:
            correct_answer == 'yes'
        elif number_1 > 3:
            for i in range(2, number_1):
                if number_1 % i == 0:
                    correct_answer = 'no'
                    break
                elif number_1 % i != 0:
                    correct_answer = 'yes'
                    continue
        print(f'Question: {number_1}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            continue
        else:
            lose += 1
            break
    return [lose, correct_answer, user_answer]