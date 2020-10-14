# THIS SCRIPT GOES BEYOND WHAT WE COVERED IN CLASS
# we will cover this next time, but I wanted to give you more to play with
# it’s a multipage document that we will save

# import our special functions from the random library
from random import randrange, random

# page dimensions
pageWidth = 1000
pageHeight = 1000

# define how many pages
numPages = 10

# define how many rows and columns
rows = 50
cols = 50

# define the width and height of each unit of the grid
gridWidth = pageWidth/rows
gridHeight = pageHeight/cols

# define the width and height of the shape we will draw in that grid
shapeWidth = pageWidth/rows
shapeHeight = pageHeight/cols

# ok it’s time to loop
# first we will loop through each row
# and then WITHIN that loop we will loop through each column
# for theThing in theRangeOfThings

# a loop for each page
for page in range(numPages):
    newPage(pageWidth, pageHeight)
    fill(0)
    rect(0, 0, width(), height())
        
    # define the width and height of the shape we will draw in that grid
    # make it a little smaller than the grid this time
    shapeWidth = pageWidth/rows - 10
    shapeHeight = pageHeight/cols - 10

    # define x and y as where we start? (0, 0) is in the bottom left
    # for each page we want to reset these
    
    # we are going to draw the shapes from the center this time, 
    # so we want our X and Y coordinates to be at the center of each grid
    x = gridWidth / 2
    y = gridHeight / 2
    
    for row in range(rows):
        # everything indented this much runs once for each row
        for col in range(cols):
            # everything indented this much runs once for each grid unit
        
            # before we draw our shape, let’s pick a color for it
            # we can create 3 variables
            r = random() # red
            g = random() # green
            b = random() # blue
            a = .8 # alpha (0 = transparent, 1 = opaque)
            fill(r, g, b, a)
    
            # okay, now we finally draw our shape
            
            # let’s define specific shape dimensions for
            # JUST THIS ONE shape
            # by using our basic dimensions and adding some randomness
            thisShapeWidth = shapeWidth + randrange(-5, 5)
            thisShapeHeight = shapeHeight + randrange(-5, 5)
            
            # we can make a conditional
            # if this condition is true:
            #    then run this code
            # if not:
            #     then run this code
            if random() > .5:
                # to draw from the center, we move the 
                # x position to the left half of its width
                # and move it down half its height
                rect(x-thisShapeWidth/2, y-thisShapeHeight/2, thisShapeWidth, thisShapeHeight)
            else:
                oval(x-thisShapeWidth/2, y-thisShapeHeight/2, thisShapeWidth, thisShapeHeight) 
            # at the end of the column, advance X to the next column
            x += gridWidth
            # let’s also make the shape a smidge bigger each time
            shapeWidth += .01
            shapeHeight += .01
        # we are OUTDENTED, which means we are back 
        # to code that only runs once per row
        # now that we’ve reached the end of the row
        # we want to advance y to move us up to the next row
        y += gridHeight
        # and we want to return x to its original position
        # (a carriage return, essentially)
        #  
        x -= cols*gridWidth
        
# now let’s save this image to the desktop
# first as a PDF
saveImage('~/desktop/myFancyGrid.pdf')
# then as a GIF
saveImage('~/desktop/myFancyGrid.gif')