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

    # Neighbour system
    # 1 2 3
    # 4 o 6
    # 7 8 9
    #
    # 1 -> array[x - 1][y - 1]
    # 2 -> array[x - 1][y]
    # 3 -> array[x - 1][y + 1]
    # 4 -> array[x][y - 1]
    # 6 -> array[x][y + 1]
    # 7 -> array[x + 1][y - 1]
    # 8 -> array[x + 1][y]
    # 8 -> array[x + 1][y + 1]


    # Elements are referenced [row][column] with starting index 0
    array = defineArray(row, col)

    plot.imshow(array, interpolation='nearest')
    plot.gray()
    plot.show()

    # Create a new grid system based on the last one
    newArray = defineArray(row, col)

    # Get the count of alive neighbour cells
    #for x in range(row):
        #for y in range(col):

    

if __name__ == '__main__': 
    main() 