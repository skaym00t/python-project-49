#!/usr/bin/env python3


def main():
    from brain_games.logic.logic_game import return_name, answer_game
    from brain_games.games.game_2 import result_game
    name_user = return_name()
    lose, correct_answer, user_answer = result_game()
    answer_game(lose, correct_answer, user_answer, name_user)


if __name__ == '__main__':
    main()
