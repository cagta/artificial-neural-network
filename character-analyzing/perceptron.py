import numpy as np

IMAGE_COLUMN_SIZE = 7
IMAGE_ROW_SIZE = 9

"""
    FONTS => Object that contains every font family will be recognized in this script.
        "first" => One of the font families
            "A" => Index arrays of each dots in the each row of the image.

    Example Point Array: 

    Character : A = [[2], [1,3], [1,2,3], [1,3]]  
    . . * . .        [2]
    . * . * .             [1,3]
    . * * * .                    [1,2,3]
    . * . * .                             [1,3]
"""
FONTS = {
    "first" : {
        "A": [[2, 3], [3], [3], [2, 4], [2, 4], [1, 2, 3, 4, 5], [1, 5], [1, 5], [0, 1, 2, 4, 5, 6]],
        "B": [[0,1,2,3,4,5], [1,6], [1,6], [1,6], [1,2,3,4,5], [1,6], [1,6], [1,6], [0,1,2,3,4,5]],
        "C": [[2,3,4,5,6], [1,6], [0], [0], [0], [0], [0], [1,6], [2,3,4,5]],
        "D": [[0,1,2,3,4], [1,5], [1,6], [1,6], [1,6], [1,6], [1,6], [1,5], [0,1,2,3,4]],
        "E": [[0,1,2,3,4,5,6],[1,6],[1],[1,3],[1,2,3],[1,3],[1],[1,6],[0,1,2,3,4,5,6]],
        "J": [[3,4,5,6],[5],[5],[5],[5],[5],[1,5],[1,5],[2,3,4]],
        "K": [[0,1,2,5,6],[1,4],[1,3],[1,2],[1,2],[1,3],[1,4],[1,5],[0,1,2,5,6]]
    },
    "second": {
        "A": [[3], [3], [3], [2,4], [2,4], [1,5], [1,2,3,4,5], [1, 5], [1, 5]],
        "B": [[0,1,2,3,4,5], [0,6], [0,6], [0,6], [0,1,2,3,4,5], [0,6], [0,6], [0,6], [0,1,2,3,4,5]],
        "C": [[2,3,4], [1,5], [0,6], [0], [0], [0],  [0,6], [1,5], [2,3,4]],
        "D": [[0,1,2,3,4], [0,5], [0,6], [0,6], [0,6], [0,6], [0,6], [0,5], [0,1,2,3,4]],
        "E": [[0,1,2,3,4,5,6],[0],[0],[0],[0,1,2,3,4],[0],[0],[0],[0,1,2,3,4,5,6]],
        "J": [[5],[5],[5],[5],[5],[5],[1,5],[1,5],[2,3,4]],
        "K": [[0,5],[0,4],[0,3],[0,2],[0,1],[0,2],[0,3],[0,4],[0,5]]
    },
    "third" : {
        "A": [[3],[3], [2, 4], [2, 4], [1,5], [1, 2, 3, 4, 5], [0,6], [0, 6],[0,1,5,6]],
        "B": [[0,1,2,3,4,5], [1,6], [1,6], [1,2,3,4,5], [1,6], [1,6], [1,6], [1,6], [0,1,2,3,4,5]],
        "C": [[2,3,4,6], [1,5,6], [0,6], [0], [0], [0], [0,6], [1,5], [2,3,4]],
        "D": [[0,1,2,3,4], [1,5], [1,6], [1,6], [1,6], [1,6], [1,6], [1,5], [0,1,2,3,4]],
        "E": [[0,1,2,3,4,5,6],[1,6],[1,3],[1,2,3],[1,3],[1],[1],[1,6],[0,1,2,3,4,5,6]],
        "J": [[4,5,6],[5],[5],[5],[5],[5],[5],[1,5],[2,3,4]],
        "K": [[0,1,2,5,6],[1,5],[1,4],[1,3],[1,2],[1,3],[1,4],[1,5],[0,1,2,5,6]]
    }
}

def printVector(charVector):
    for i in range(0,IMAGE_ROW_SIZE):
        for j in range(0, IMAGE_COLUMN_SIZE):
            print ("%2d" %(charVector[IMAGE_COLUMN_SIZE*i+j]), end=' ')
        print("")

def printChar(charVector):
    for i in range(0,IMAGE_ROW_SIZE):
        for j in range(0, IMAGE_COLUMN_SIZE):
            if (charVector[IMAGE_COLUMN_SIZE*i+j] == -1):
                print ('%2s' % ("#"), end=' ')
            else:
                print ("%2s" %('.'), end=' ')
        print("")

def drawChar(font):
    """
        This function prepares vectors for each character in the font family

        param: Object that contains every font family will be recognized in this script

        return: List of the vectors of the font family
    """
    charList = []
    for key, char in font.items():
        charVector = np.ones(63)
        for i in range(0,IMAGE_ROW_SIZE):
            for j in range(0, IMAGE_COLUMN_SIZE):
                if (j in char[i]):
                    charVector[IMAGE_COLUMN_SIZE*i+j] = -1
        charList.append(charVector)
    return charList

def prepareInputs(fonts):
    """
        This function prepare all vectors for font families and stores them into list.

        param: Object that contains every font family will be recognized in this script

        return: List of the vectors of each font family 
    """
    inputList = []
    for key, font in FONTS.items():
        inputList.append(drawChar(font))
    return inputList

inputVectors = prepareInputs(FONTS)
for font in inputVectors:
    for char in font:
        printChar(char)
        printVector(char)
        break