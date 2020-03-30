from threading import Thread
from numpy import zeros
from random import randrange
from matplotlib import pyplot as plot
from matplotlib import animation, rcParams

width, height = 400, 400
dotres = 10

global col, row
col = int(width/dotres)
row = int(height/dotres)

def defineArray(nrow, ncol):
    # Elements are referenced [row][column] with starting index 0
    array = zeros((nrow, ncol))
    for x in range(nrow):
        for y in range(ncol):
            array[x][y] = randrange(0,2)
    return array

global ogScene, nextScene
ogScene = defineArray(row, col)
nextScene = defineArray(row, col)

def neighbourCellCounter(array, xo, yo):
    # xo, yo - center cell position
    # Go around the neighbour cells
    # Count the alive ones

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

    global col, row
    aliveSum = 0
    for x in range(-1,2):
        for y in range(-1,2):

            rows = (xo + x + row) % row
            cols = (yo + y + col) % col

            aliveSum += array[rows][cols]
    aliveSum -= array[xo][yo]
    return aliveSum

fig, ax = plot.subplots()
counter = 0


def main():

    def countAlive():
        global nextScene, counter
        for x in range(row):
            for y in range(col):
                if nextScene[x][y] == 1:
                    counter += 1

    def updateGrid(i):

        # Create a new thread after last one finished
        thread2 = Thread(target=countAlive())
        thread2.start()

        # Create a new grid system based on the last one
        global ogScene, nextScene, counter
        nextScene = defineArray(row, col)
        for x in range(row):
            for y in range(col):
                nSum = neighbourCellCounter(ogScene, x, y)
                cellState = ogScene[x][y]
                if cellState == 0 and nSum == 3:
                    nextScene[x][y] = 1
                elif cellState == 1 and (nSum < 2 or nSum > 3):
                    nextScene[x][y] = 0
                else:
                    nextScene[x][y] = cellState
        ogScene = nextScene
        thread2.join() # Wait until the last thread was completed
        ax.cla()
        ax.imshow(nextScene)
        ax.set_axis_off()
        ax.set_title("Alive cells: " + str(counter))
        fig.canvas.toolbar.pack_forget()
        counter = 0

    plot.gray()
    ani = animation.FuncAnimation(fig, updateGrid, frames=20, interval=2)
    plot.show()


if __name__ == '__main__': 
    thread1 = Thread(target=main())
    thread1.start()


