def result_game():
    print('What number is missing in the progression?')
    import prompt
    import random
    lose = 0
    correct_answer = ''
    user_answer = ''
    for i in range(3):
        progression = []
        number_1 = random.randint(1, 50)
        number_2 = random.randint(4, 12)
        progression.append(number_1)
        for i in range(11):
            progression.append(progression[-1] + number_2)
        random_index = random.randint(0, 9)
        correct_answer = str(progression[random_index])
        progression[random_index] = '..'
        str_progression = ''
        for i in progression:
            str_progression = str_progression + str(i) + ' '
        str_progression = str_progression.strip()
        print(f'Question: {str_progression}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            continue
        else:
            lose += 1
            break
    return [lose, correct_answer, user_answer]
