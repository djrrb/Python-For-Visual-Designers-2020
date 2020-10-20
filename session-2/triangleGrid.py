from random import random

def triangle(x, y, w, h):
    polygon((x, y), (x+w/2, y+h), (x+w, y))

for page in range(1):
    newPage(1000, 1000)
    # loop for rows
    #fill(1, 1, 1)
    #rect(0, 0, width(), height())
    for y in range(0, height(), 50):
        # loop for columns
        for x in range(0, width(), 50):
            # draw oval or rectangle
            fill(random(), random(), random())
            if random() < 1/3:
                triangle(x, y, 50, 50)
            elif random() < 2/3:
                oval(x, y, 50, 50)
            else:
                rect(x, y, 50, 50)
            
#saveImage('~/desktop/myCoolGrid.png')