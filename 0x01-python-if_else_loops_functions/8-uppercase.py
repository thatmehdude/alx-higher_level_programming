#!/usr/bin/python3


def uppercase(str):
    for c in range(len(str)):
        alphabet = ord(str[c])
        if (alphabet >= 97) and (alphabet <= 122):
            alphabet = alphabet - 32
            print('{}'.format(chr(alphabet), end=''))
    print()
