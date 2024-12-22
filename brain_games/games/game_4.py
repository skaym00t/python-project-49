def result_game():
    print('What number is missing in the progression?')
    import prompt
    import random
    lose = 0
    correct_answer = ''
    user_answer = ''
    for i in range(3):
        progression = [] # создаем прогрессию
        number_1 = random.randint(1, 50) # стартовое число
        number_2 = random.randint(4, 12) # шаг прогрессии
        progression.append(number_1) # помещаем первое число в прогрессию
        for i in range(11):
            progression.append(progression[-1] + number_2) # считаем и помещаем остальные числа
        random_index = random.randint(0, 9) # берем рандомный индекс
        correct_answer = str(progression[random_index]) # выбираем корректный ответ
        progression[random_index] = '..' # заменяем его на пропущенное значение
        str_progression = '' # создаем строку для вывода пользователю
        for i in progression:
            str_progression = str_progression + str(i) + ' ' # заполняем строку
        str_progression = str_progression.strip() # обрезаем пробелы по краям
        print(f'Question: {str_progression}') # выводим строку пользователю
        user_answer = prompt.string('Your answer: ') # запрашиваем ответ
        if user_answer == str(correct_answer): # проверяем совпал ли он с корректным
            print('Correct!')
            continue
        else:
            lose += 1
            break
    return [lose, correct_answer, user_answer]
