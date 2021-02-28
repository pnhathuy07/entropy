import re

import functions as f
from functions import inp

keydict = {' ' : 16, 'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

def encode():
    decodedict = getDecodeDict('Please type in the key that you want. You will use this key later to decode the file.')
    destroy(decodedict, 1)

def decode():
    decodedict = getDecodeDict('Please input the key to decode the file.')
    destroy(decodedict, -1)

def getDecodeDict(message):
    key = ' '.join(re.split(f'[^A-Z]+', inp(message, 'key').upper()))
    decodedict = []
    for letter in key:
        decodedict.append(keydict[letter])
    return decodedict


def destroy(decodedict, DIR):
    filename = f.dragdrop()
    with open(filename, "rb") as binaryfile:
        myArr = bytearray(binaryfile.read())
        for i in range(len(myArr)):
            newByte = myArr[i] + DIR * decodedict[i % len(decodedict)]
            if newByte > 255: newByte -= 255
            if newByte < 0: newByte += 255

            myArr[i] = newByte

    with open(filename, "wb") as newFile:
        newFile.write(myArr)