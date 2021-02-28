import random

import functions as f
from functions import inp

def destroy():
    percentage = int(inp('How many percent do you want your file to be detroyed? (From 0 to 100)', 'percentage', '100'))
    filename = f.dragdrop()
    with open(filename, "rb") as binaryfile:
        myArr = bytearray(binaryfile.read())
        for i in range(len(myArr)):
            if (random.randint(1, 100) <= percentage): myArr[i] = myArr[0 - random.randint(0, len(myArr))]

    with open(filename, "wb") as newFile:
        newFile.write(myArr)