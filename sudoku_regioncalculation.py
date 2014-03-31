import random
import time

def getAcross(x):
    i = x % 9
    if i == 0:
        return 9
    else:
        return i

def getDown(x):
    if getAcross(x) == 9:
        i = int(x/9)
    else:
        i = int(x/9) + 1
    return i

def getRegion(x):
    c = getAcross(x) - 1
    r = getDown(x) - 1
    return ((r//3) + (3 * (c//3))) + 1

class Square:
    across = 0 #column
    down = 0 #row
    region = 0 #box
    value = 0
    index = 0
    
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.across = getAcross(index+1)
        self.down = getDown(index+1)
        self.region = getRegion(index+1)        

def conflict(test, squares):
    for s in squares:
        if ((s.across == test.across) or (s.down == test.down) or (s.region == test.region)):
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
            value = random.choice(available[index])
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
    #printboard(currentSquares)
    #print('---------')
    return (end - start)
    
i = 0
x = 25000
total = 0
while i < x:
    total = total + generateBoard()
    i = i + 1
print(total/x)
