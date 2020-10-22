# argyle (?) sock pattern
size('TabloidLandscape')

# set some constants

# number of columns
columns = 5

# from the number of columns, we can automatically calculate the width of each column
w = width()/columns

# give each stripe a height
h = 75

# start X at the left hand edge
x = 0

# start Y one stripe height below zero so we never see the bottom 
y = -h

# o is the parallelogram offset from the straight segment on left to the straight segment on right. This determines the angle of the diagonal stripes...
o = height()/5

# draw the background rectangles
for col in range(columns):
    # use the remainder (%) operator to alternate colors for even/odd columns
    # an even number / 2 will have 0 remainder
    # an odd number / 2 will have 1 remainder
    if col % 2 == 0: 
        fill(1)      # even number, starting with 0
    else:
        fill(1,0,.5) # odd number
        
    # draw a rectangle the height of the page 
    rect(x, 0, w, height())
    # augment x so we are ready to draw the next column
    x += w
    

# now let’s reset to 0 to draw the stripes
x = 0

# loop through each column
for col in range(columns):

    # alternate each column between overlay and multiply blend modes. this will create new colors where our shapes overlap!
    if col % 2 == 0:
        blendMode('multiply')    
    else:
        blendMode('overlay')

    # use a while loop to keep drawing stripes until we reach the top of our document...when the y variable becomes greater than the document height, stop the loop
    while y < height():
        
        # within each stripe loop, we’re gonna draw two stripes: one ascending, one descending
        
        # use the % again to alternate color for even/odd columns
        if col % 2 == 0:
            fill(1, 0, .5)
        else:
            fill(1, .5, 1)
            
        # draw the ascending polygon
        # adding the o (offset)
        polygon(
            (x, y+o), 
            (x+w, y), 
            (x+w, y+h), 
            (x, y+h+o)
        )
        
        # now do it all again for the descending polygon
        if col % 2 == 0:
            fill(0, .5, 1)
        else:
            fill(0, 1, 0)
        polygon(
            (x, y), 
            (x+w, y+o), 
            (x+w, y+h+o), 
            (x, y+h)
        )
        
        # augment the y variable so that the next set of stripes is higher
        y += o
        
    # once we reach the top of the column, reset some variables so we’re ready for the next column 
    x += w
    y = -h
    
