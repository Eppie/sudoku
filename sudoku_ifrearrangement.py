import random
from random import choice
import time

def getAcross(x):
    i = 0
    i = x % 9
    if i == 0:
        return 9
    else:
        return i

def getDown(x):
    i = 0
    if getAcross(x) == 9:
        i = int(x/9)
    else:
        i = int(x/9) + 1
    return i

def getRegion(x):
    i = 0
    a = getAcross(x)
    d = getDown(x)
    if 1 <= d and d < 4:
        if 1 <= a and a < 4:
            i = 1
        if 4 <= a and a < 7:
            i = 2
        if 7 <= a and a < 10:
            i = 3
    elif 4 <= d and d < 7:
        if 1 <= a and a < 4:
            i = 4
        if 4 <= a and a < 7:
            i = 5
        if 7 <= a and a < 10:
            i = 6
    elif 7 <= d and d < 10:
        if 1 <= a and a < 4:
            i = 7
        if 4 <= a and a < 7 :
            i = 8
        if 7 <= a and a < 10:
            i = 9
    return i

class Square:
    across = 0 #column
    down = 0 #row
    region = 0 #box
    value = 0
    index = 0
    whole = []
    
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.across = getAcross(index+1)
        self.down = getDown(index+1)
        self.region = getRegion(index+1)
        self.whole = ['col: ' + str(self.across), 'row: ' + str(self.down), 'box: ' + str(self.region), 'val: ' + str(self.value), self.index]
        
        
def getRan(l):
    return choice(l)

def conflict(test, squares):
    for s in squares:
        if ((s.across != 0 and s.across == test.across) or (s.down != 0 and s.down == test.down) or (s.region != 0 and s.region == test.region)):
            if s.value == test.value:
                return True
    return False

def printboard(board):
    i = 1
    for square in board:
        print(square.value,end='')
        if i % 9 == 0:
            print('')
        i = i + 1
        
def generateBoard():
    start = time.clock()
    currentSquares = [Square(0,0) for x in range(81)]
    available = [[1,2,3,4,5,6,7,8,9] for x in range(81)]
    index = 0
    while index < 81:
        if len(available[index]) != 0:
            value = getRan(available[index])
            test = Square(value, index)
            if not conflict(test, currentSquares):
                currentSquares[index] = Square(test.value, test.index)
                available[index].remove(value)
                index = index + 1
            else:
                available[index].remove(value)
        else:
            available[index] = [1,2,3,4,5,6,7,8,9]
            currentSquares[index] = Square(0,0)
            index = index - 1
    end = time.clock()
    return (end - start)
    #printboard(currentSquares)
    
i = 0
x= 5000
total = 0
while i < x:
    total = total + generateBoard()
    i = i + 1
print(total/x)
