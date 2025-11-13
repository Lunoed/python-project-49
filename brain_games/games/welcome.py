import prompt


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have yout name? ')
    print(f'Hello, {name}.')
    return name
