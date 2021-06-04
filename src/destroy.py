import random
import functions as f
from functions import inp


def destroy():
    percentage = int(inp('What percentage do you want your file to be destroyed? (From 0 to 100)',
                         assign='percentage', default='100'))
    filename = f.drag_drop()

    with open(filename, "rb") as binary_file:
        myArr = bytearray(binary_file.read())
        for i in range(len(myArr)):
            if random.randint(1, 100) <= percentage:
                myArr[i] = myArr[0 - random.randint(0, len(myArr))]

    with open(filename, "wb") as newFile:
        newFile.write(myArr)
