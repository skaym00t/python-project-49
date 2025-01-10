#!/usr/bin/env python3


def main():
    from brain_games.logic.logic_game import return_name, run_game
    from brain_games.games.game_4 import result_game

    run_game(return_name(), result_game())


if __name__ == "__main__":
    main()
