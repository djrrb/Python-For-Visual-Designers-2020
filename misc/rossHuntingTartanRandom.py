# a random plaid generator based on the Ross Hunting Tartan
# https://www.heritageofscotland.com/tartans/ross-hunting-ancient/870

# This is not a particularly clever or elegantly-written script. I’m sure there are more efficient ways to define this pattern, but I just decided to draw a bunch of rects and then shift the numbers around until it looked right

# import the colorsys library so we can translate HSV to RGB
# hue, saturation, value
import colorsys

# determine the number of pages
thePages = 10

# loop through the pages
for page in range(thePages):

    # determine the number of times we want to tile the basic pattern
    tile = randint(1, 5)
    
    # on the first page, always use the authentic Ross Tartan colors
    if page == 0:
        red = 1, .2, .2, 1
        darkGreen = 0, 0, 0, .5
        lightGreen = 178/255, 206/255, 93/255, .5
        bg = 12/255, 114/255, 85/255
    # otherwise do something semi-random
    else: 
        # calculate a random hue value to be the base
        baseHue = random()
        # now vary the saturation and value predictably 
        # to get some complementary colors
        
        # the background should be a mid-range color, not too dark or bright
        bg = colorsys.hsv_to_rgb(baseHue, .6, .5)
        # this should always be a contrasting color and light and bright
        red = colorsys.hsv_to_rgb(abs(baseHue-.3), .8, 1)
        # dark green should be a darker version of the background
        darkGreen = colorsys.hsv_to_rgb(baseHue, 1, .3)
        # these stripe should be saturated but not necessarily super bright
        lightGreen = colorsys.hsv_to_rgb(abs(baseHue-.1), .8, .7)

        
    # make a new page 
    newPage(1000, 1000)
    # if we’re animating, slow it down
    # by setting the frame duration to a portion
    # of a second
    frameDuration(.3)

    # fill the background with a big rectangle
    fill(*bg)
    rect(0, 0, width(), height())

    # determine the size of each tile
    w = width()//tile
    h = height()//tile

    # this is a little hacky
    # this value is esssentially the base width of a stripe
    # relative to the width of a tile
    # by making all stripe widths relative to this
    # it’s easier to unitize the rhythm of the stripes
    b = 6.85/1000*w

    startX = startY = 0
    # if we wanted to center, we could offset the start positions
    #startX = startY = int(-b*3.5)

    # do a grid
    for y in range(startY, height()+h, h):
        for x in range(startX, width()+w, w):
            # set the blend mode to overlay so that we see the overlaps
            blendMode('overlay')
            ##########
            # let the rectangle avalanche begin!
            ########## 
            # draw our skinny three lines (red by default)
            fill(*red)
            # horizontal
            rect(x, y, w, b)
            rect(x, y+b*3, w, b)
            rect(x, y+b*6, w, b)
            rect(x, y+b*69, w, b)
            rect(x, y+b*72, w, b)
            rect(x, y+b*75, w, b)
            # vertical
            rect(x, y, b, h)
            rect(x+b*3, y, b, h)
            rect(x+b*6, y, b, h)
            rect(x+b*69, y, b, h)
            rect(x+b*72, y, b, h)
            rect(x+b*75, y, b, h)
            blendMode('overlay')
            # draw our thick darker lines
            # dark green by default
            fill(*darkGreen)
            # horizontal, set one
            rect(x, y+b*21, w, b*3)
            rect(x, y+b*26, w, b*3)
            rect(x, y+b*47, w, b*3)
            rect(x, y+b*52, w, b*3)
            # horizontal, set 2
            rect(x, y+b*90, w, b*3)
            rect(x, y+b*95, w, b*3)
            rect(x, y+b*124, w, b*3)
            rect(x, y+b*129, w, b*3)
            # vertical, set 1
            rect(x+b*21, y, b*3, h)
            rect(x+b*26, y, b*3, h)
            rect(x+b*47, y, b*3, h)
            rect(x+b*52, y, b*3, h)
            # vertical, set 2 
            rect(x+b*90, y, b*3, h)
            rect(x+b*95, y, b*3, h)
            rect(x+b*124, y, b*3, h)
            rect(x+b*129, y, b*3, h)
            # now the lighter skinny bars
            # light green by default
            fill(*lightGreen)
            # horizontal, set 1
            rect(x, y+b*32, w, b)
            rect(x, y+b*35, w, b)
            rect(x, y+b*40, w, b)
            rect(x, y+b*43, w, b)
            # horizontal, set 2
            rect(x, y+b*101, w, b)
            rect(x, y+b*104, w, b)
            rect(x, y+b*107, w, b*3)
            rect(x, y+b*112, w, b*3)
            rect(x, y+b*117, w, b)
            rect(x, y+b*120, w, b)
            # vertical, set 1
            rect(x+b*32, y, b, h)
            rect(x+b*35, y, b, h)
            rect(x+b*40, y, b, h)
            rect(x+b*43, y, b, h)
            # vertical, set 2
            rect(x+b*101, y, b, h)
            rect(x+b*104, y, b, h)
            rect(x+b*107, y, b*3, h)
            rect(x+b*112, y, b*3, h)
            rect(x+b*117, y, b, h)
            rect(x+b*120, y, b, h) 

saveImage('~/desktop/ross-hunting-tartan-ancient-random.gif')