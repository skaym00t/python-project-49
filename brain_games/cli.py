def welcome_user():
    import prompt
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
