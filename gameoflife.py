from threading import Thread
from numpy import zeros
from random import randrange
from matplotlib import pyplot as plot
from matplotlib import animation

width, height = 400, 400
dotres = 10

global col, row
col = int(width/dotres)
row = int(height/dotres)

def defineArray(row, col):
    # Elements are referenced [row][column] with starting index 0
    array = zeros((row, col))
    for x in range(row):
        for y in range(col):
            array[x][y] = randrange(0,2)
    return array

global ogScene
ogScene = defineArray(row, col)

def neighbourCellCounter(array, xo, yo):
    # xo, yo - center cell position
    # Go around the neighbour cells
    # Count the alive ones

    global col, row
    aliveSum = 0
    for x in range(-1,2):
        for y in range(-1,2):

            rows = (xo + x + row) % row
            cols = (yo + y + col) % col

            aliveSum += array[rows][cols]
    aliveSum -= array[xo][yo]
    return aliveSum

def updateGrid(i):
    # Create a new grid system based on the last one
    nextScene = defineArray(row, col)
    global ogScene
    for x in range(row-1):
        for y in range(col-1):
            cellState = ogScene[x][y]
            nSum = neighbourCellCounter(ogScene, x, y)
            if cellState == 0 and nSum == 3:
                nextScene[x][y] = 1
            elif cellState == 1 and (nSum < 2 or nSum > 3):
                nextScene[x][y] = 0
            else:
                nextScene[x][y] = cellState
    ogScene = nextScene
    ax.cla()
    ax.imshow(nextScene)

# Neighbour cells system
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
# 9 -> array[x + 1][y + 1]

fig, ax = plot.subplots()
matrice = ax.matshow(ogScene)
plot.gray()

ani = animation.FuncAnimation(fig, updateGrid, frames=60, interval=20)
plot.show()
