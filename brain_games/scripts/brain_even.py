#!/usr/bin/env python3


def main():
    from .brain_games import main
    name_user = main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    from brain_games.game_1 import first_game
    lose, correct_answer, user_answer = first_game()
    if lose != 0:
       return print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {name_user}!''')
    else:
        print(f'Congratulations, {name_user}!')


if __name__ == '__main__':
    main()
    