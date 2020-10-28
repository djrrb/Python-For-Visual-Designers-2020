# loop through each page
for angle in range(0, 360, 2):
    # make a new page and a white background
    newPage(1000, 1000)
    fill(1)
    rect(0, 0, width(), height())
    
    # start drawing rectangles at the full width and height
    w, h = width(), height()
    
    # move our origin to the center
    translate(width()/2, height()/2)

    # scale by a certain amount    
    scaleValue = .97
    # keep track of our total scale (optional)
    totalScale = 1

    # draw a bunch of rectangles
    # shrinking and rotating the canvas each time
    
    for rectangleIndex in range(200):
        # red stroke, no fill
        stroke(1, 0, 0)
        fill(None)

        # we didn’t talk about this in class
        # if we set the stroke width each time
        # we can reverse the effects of the scaling
        strokeWidth(1/totalScale)
        
        # draw our rect
        rect(-w/2, -h/2, w, h)
        
        # shrink the canvas by a little
        scale(scaleValue)
        # keep track of how much we shrink the canvas by
        totalScale *= scaleValue
        # rotate the canvas
        rotate(angle)
       
# save animation
#saveImage('~/desktop/myCoolSpiral.gif')