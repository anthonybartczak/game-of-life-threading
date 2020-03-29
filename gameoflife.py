from threading import Thread
from numpy import zeros
from random import randrange
from matplotlib import pyplot as plot

width, height = 600, 400
dotres = 20

col = int(width/dotres)
row = int(height/dotres)

def defineArray(row, col):
    array = zeros((row, col))
    for x in range(row):
        for y in range(col):
            array[x][y] = randrange(0,2)
    return array

def updateGrid():
    pass

def main():

    array = defineArray(row, col)
    newArray = defineArray(row, col)

    plot.imshow(array, interpolation='nearest')
    plot.gray()
    plot.show()
    

if __name__ == '__main__': 
    main() 