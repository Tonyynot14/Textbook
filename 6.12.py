import random


def printChars(ch1,ch2,numberPerLine):

    for i in range(numberPerLine):
        print(chr(random.randint(ord(ch1),ord(ch2))),end=" ")
    print()


printChars("1","Z",10)