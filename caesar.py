#!/usr/bin/python3

import helpers
from sys import argv

# Use your desired rotation amount as an argument when running this program


def encrypt(text, rot):
    new_string = []
    for i in text:
        new_string.append(helpers.rotate_character(i, rot))
    return "".join(new_string)


def main():
    user_input = input("Type a message: ")
    if len(argv) > 1:
        rotation_factor = int(argv[1])
    else:
        rotation_factor = int(input("Type a rotation factor: "))
    print(encrypt(user_input, rotation_factor))


if __name__ == "__main__":
    main()
