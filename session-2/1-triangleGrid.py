from random import random

# drawbot doesn’t have a function for triangle
# so let’s make one
# we use the def keyword to define
# a function called "triangle"
# and then say that it must receive 
# four arguments: x, y, w, h

def triangle(x, y, w, h):
    # now, within the triangle function
    # we will use the built-in drawbot
    # polygon() function, which takes a sequence
    # of (x, y) coordinates
    polygon((x, y), (x+w/2, y+h), (x+w, y))

# loop through the number of pages
for page in range(1):
    # make a new page each time
    newPage(1000, 1000)

    # draw a white background the full size of the canvas
    # use the width() and height() functions to get the
    # width and height of the document
    fill(1, 1, 1)
    rect(0, 0, width(), height())

    # loop for the y coordinate, stepping 50 each time
    for y in range(0, height(), 50):
        # loop for the x coordinaet, stepping 50 each time
        for x in range(0, width(), 50):
            # gimme a random color
            fill(random(), random(), random())
            # draw oval or rectangle or triangle or text
            # get a random number between 0 and 1
            # and then use an if statement to go through
            # what we want to happen for each possibility
            randomNumber = random()
            if randomNumber < 1/4:
                # gimme a triangle
                triangle(x, y, 50, 50)
            elif randomNumber < 2/4:
                # gimme an oval
                oval(x, y, 50, 50)
            elif randomNumber < 3/4:
                # gimme a rectangle
                rect(x, y, 50, 50)
            else:
                # gimme some text
                fontSize(70)
                font('Georgia')
                text('H', (x, y))

# this last line will save the image
# the format will change depending on the
# extension of the file
# pdf, png, jpg, jpeg, tif, tiff, svg, gif, bmp, mp4, mov (not really), icns

#saveImage('~/desktop/myCoolGrid.png')