#!/usr/bin/python3
def uppercase(str):
    word = ""
    for index in str:
        char = ord(index)
        if char >= 97 and char <= 122:
            word = word + chr(char - 32)
        else:
            word = word + index
    print("{:s}".format(word))
