#!/usr/bin/env python3

def return_name():
    print('Welcome to the Brain Games!')
    from brain_games.cli import welcome_user
    name = welcome_user()
    return name


def run_game(name_user, game):
    lose, correct_answer, user_answer = game

    def answer_game(lose, correct_answer, user_answer, name_user):
        if lose != 0:
            return print(f'''"{user_answer}" is wrong answer ;(.
Correct answer was "{correct_answer}".
Let's try again, {name_user}!''')
        else:
            print(f'Congratulations, {name_user}!')
    answer_game(lose, correct_answer, user_answer, name_user)
