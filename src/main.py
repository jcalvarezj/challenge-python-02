# Resolve the problem!!
import string
from random import randint


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LOWER = 0
UPPER = 1
SYMBOL = 2
NUMBER = 3
LOWER_START = 97
LOWER_END = 122
UPPER_START = 65
UPPER_END = 90
MIN_SIZE = 8
MAX_SIZE = 16


def generate_password():
    password = ''
    length = randint(MIN_SIZE, MAX_SIZE)
    for index in range(0, length):
        character = ''
        char_type = randint(0, 3)

        if index % 7 == 0:
            char_type = SYMBOL
        elif index % 5 == 0:
            char_type = NUMBER
        elif index % 3 == 0:
            char_type = UPPER
        elif index % 2 == 0:
            char_type = LOWER            

        if char_type == LOWER:
            character = chr(randint(LOWER_START, LOWER_END))
        elif char_type == UPPER:
            character = chr(randint(UPPER_START, UPPER_END))
        elif char_type == SYMBOL:
            character = SYMBOLS[randint(0, len(SYMBOLS) - 1)]
        else:
            character = f'{randint(0, 9)}'

        password += character
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
