import re
import functions as f
from functions import inp


def encrypt():
    decode_key = get_decode_key('Please type in the key that you want.'
                                'You will use this key later to decode the file.')
    modify(decode_key, 1)


def decrypt():
    decode_dict = get_decode_key('Please input the key to decode the file.')
    modify(decode_dict, -1)


# --------------------------------------- Encrypting Algorithm --------------------------------------- #
key_dict = {' ': 16, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
            'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
            'Y': 25, 'Z': 26}


def get_decode_key(message):
    key = ' '.join(re.split(f'[^A-Z]+', inp(message, assign='key').upper()))
    decode_dict = []
    for letter in key:
        decode_dict.append(key_dict[letter])
    return decode_dict


def modify(decode_dict, direction):
    """Modify the file."""
    filename = f.drag_drop()
    with open(filename, "rb") as binary_file:
        myArr = bytearray(binary_file.read())
        for i in range(len(myArr)):
            newByte = myArr[i] + direction * decode_dict[i % len(decode_dict)]
            if newByte > 255:
                newByte -= 255
            if newByte < 0:
                newByte += 255

            myArr[i] = newByte

    with open(filename, "wb") as newFile:
        newFile.write(myArr)
