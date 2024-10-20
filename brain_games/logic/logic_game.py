#!/usr/bin/env python3

def return_name():
    from brain_games.scripts.brain_games import main
    return main()


def answer_game(lose, correct_answer, user_answer, name_user):
    if lose != 0:
        return print(f'''"{user_answer}" is wrong answer ;(.
Correct answer was "{correct_answer}".
Let's try again, {name_user}!''')
    else:
        print(f'Congratulations, {name_user}!')
