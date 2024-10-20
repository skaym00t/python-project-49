def result_game():
    print('Find the greatest common divisor of given numbers.')
    import prompt
    import random
    lose = 0
    correct_answer = ''
    user_answer = ''
    for i in range(3):
        gcd = []  # список общих делителей
        while len(gcd) < 2:  # ищем 2 числа минимум с 2 общими делителями
            gcd = []  # обнуляем список, если общих делителей меньше 2
            number_1 = random.randint(1, 100)  # первое рандомное число
            number_2 = random.randint(1, 100)  # второе рандомное число
            if number_1 > number_2:
                smaller = number_2
            else:
                smaller = number_1
            for i in range(2, smaller + 1):  # ищем общие делители в интервале
                if ((number_1 % i == 0) and (number_2 % i == 0)):
                    gcd.append(i)  # добавить делитель в список общих делителей
        correct_answer = gcd[-1]  # корректный ответ равен наибольшему делителю
        print(f'Question: {number_1} {number_2}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            continue
        else:
            lose += 1
            break
    return [lose, correct_answer, user_answer]
