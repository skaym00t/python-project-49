#!/usr/bin/env python3


def main():
    print('Welcome to the Brain Games!')
    from brain_games.cli import welcome_user
    name = welcome_user()
    return name


if __name__ == '__main__':
    main()
