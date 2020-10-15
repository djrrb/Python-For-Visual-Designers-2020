# import our special functions from the random library
from random import randrange, random

# define the width and height of the new page
#       w     h
newPage(1000, 1000)

# define x and y as where we start? (0, 0) is in the bottom left
x = 0
y = 0

# define how many rows and columns
rows = 10
cols = 10

# define the width and height of each unit of the grid
gridWidth = 100
gridHeight = 100

# define the width and height of the shape we will draw in that grid
shapeWidth = 100
shapeHeight = 100

# ok it’s time to loop
# first we will loop through each row
# and then WITHIN that loop we will loop through each column
# for theThing in theRangeOfThings

for row in range(rows):
    # everything indented this much runs once for each row
    for col in range(cols):
        # everything indented this much 
        # runs once for each column within 
        # each row (one grid unit)
        # before we draw our shape, let’s pick a color for it
        # we can create 3 variables
        r = random() # red
        g = random() # green
        b = random() # blue
        fill(r, g, b)
    
        # okay, now we finally draw our shape
        # we can make a conditional
        # if this condition is true:
        #    then run this code
        # if not:
        #     then run this code
        
        if random() > .5:
            rect(x, y, shapeWidth, shapeHeight+randrange(-10, 10))
        else:
            oval(x, y, shapeWidth, shapeHeight+randrange(-10, 10))
            
        # at the end of the column, advance X to the next column
        x += gridWidth
    # we are OUTDENTED, which means we are back 
    # to code that only runs once per row
    # now that we’ve reached the end of the row
    # we want to advance y to move us up to the next row
    y += gridHeight
    # and we want to return x to its original position
    # (a carriage return, essentially)
    x -= cols*gridWidth