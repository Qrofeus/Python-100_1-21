# input
# Get password length
# symbols count in password
# digit count in password
# output
# randomly generated password based on inputs

from string import ascii_letters as letters, digits, punctuation as symbols
from random import choice, shuffle

if __name__ == '__main__':
    length = int(input("Password length:\n>>"))
    symbol_count = int(input("Symbol count:\n>>"))
    digit_count = int(input("Digit count:\n>>"))
    # Implement fail check... symbol_count and digit_count greater than password length
    char_count = length - symbol_count - digit_count

    new_password = []
    for _ in range(symbol_count):
        new_password.append(choice(symbols))

    for _ in range(digit_count):
        new_password.append(choice(digits))

    for _ in range(char_count):
        new_password.append(choice(letters))

    shuffle(new_password)
    print(f'Your new password: {"".join(new_password)}')

