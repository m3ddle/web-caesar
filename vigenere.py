#!/usr/bin/python3

# IDEA: Put the encryption word into a string. Loop through the string
# if index in string == len(string):
#   counter = 0
# use a counter to keep track of where you are in the string and reset new_char
# when you get to the last character.


import helpers
import caesar
from sys import argv

# Use your desired rotation amount as an argument when running this program


def encrypt(text, encryption_key):
    counter = 0
    new_text = []
    for char in text:
        if char.isalpha():
            if counter < len(encryption_key) - 1:
                new_text.append(caesar.encrypt(
                    char, helpers.alphabet_position(encryption_key[counter])))
                counter += 1
            elif counter == len(encryption_key) - 1:
                new_text.append(caesar.encrypt(
                    char, helpers.alphabet_position(encryption_key[counter])))
                counter = 0
        else:
            new_text.append(char)
    return "".join(new_text)


def main():
    user_text = input("Type a message: ")
    if len(argv) > 1:
        user_key = argv[1]
    else:
        user_key = input("Type an encryption key: ")
    print(encrypt(user_text, user_key))


if __name__ == "__main__":
    main()
