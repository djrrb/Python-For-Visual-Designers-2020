from random import random, randrange

newPage(1000, 1000)
x = 0
y = 0

rows = 50
cols = 50

cellWidth = 20
cellHeight = 20

shapeWidth = 20
shapeHeight = 20

jitterMin = -1
jitterMax = 1

# loop through all the rows
for row in range(rows):
    # loop through all the columns
    for col in range(cols):
        # fill a random color
        fill(random(), random(), random())
        #   x, y, w, h
        # draw my oval or rect
        if random() > .5:
            rect(x, y, shapeWidth+randrange(jitterMin, jitterMax), shapeHeight+randrange(jitterMin, jitterMax))
        else:
            oval(x, y, shapeWidth+randrange(jitterMin, jitterMax), shapeHeight+randrange(jitterMin, jitterMax))
        # move the x value to the right
        x += cellWidth
        # x = x + 100
    # move the y value up 
    y += cellHeight
    # carriage return line
    x -= cols*cellWidth