#!/usr/bin/env python3

'''
WinKeyGen - Windows 10 Key Generator
Made by [Stadof](https://github.com/stadof)
'''

import random
from string import ascii_uppercase, digits

CHARACTERS = ascii_uppercase + digits
TEMPLATE = "XXXXX-XXXXX-XXXXX-XXXXX-XXXXX"


def print_banner() -> None:
    '''
    Prints the banner for the program.
    '''

    lines = [
        "             ------------------------------------------",
        "             ~~~~~~~~ WINDOWS 10 KEY GENERATOR ~~~~~~~~",
        "             ------------------------------------------",
        "",
        "             (C) 2024 Stadof",
        "             Licensed under the GNU GENERAL PUBLIC LICENSE",
        "",
        "This program uses Microsoft's algorithm to generate random Windows 10 keys",  # this is a lie, but it sounds good
        "   Feel free tu run the program several times to find a working key",
        "                  --- NOT ALL KEYS WILL WORK ---"
    ]
    print("\n".join(lines))


def generate_key(
) -> str:
    '''Generates a random Windows 10 product key.'''

    key_without_dashes = random.choices(CHARACTERS, k=25)
    key = TEMPLATE

    # sequentially fill in the template with the characters from key_without_dashes
    for char in key_without_dashes:
        key = key.replace("X", char, 1)
    return key


def main() -> None:
    '''Main function to run the key generator.'''
    amount_of_keys = 25
    print_banner()
    print("\n\n - Keys - \n")
    for _ in range(amount_of_keys):
        print(generate_key())
    input("\nPress Enter to exit...")


if __name__ == '__main__':
    main()
