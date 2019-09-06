import string


def alphabet_position(letter):
    if letter.lower() in string.ascii_lowercase:
        return string.ascii_lowercase.index(letter.lower())


def rotate_character(char, rot):
    if char.isalpha():
        if char in string.ascii_lowercase:
            return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]
        elif char in string.ascii_uppercase:
            return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    else:
        return char
