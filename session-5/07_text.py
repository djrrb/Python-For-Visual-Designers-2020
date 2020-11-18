def norm(value, start, stop):
    """
    Map a value between 0 and 1 and return the corresponding position between start and stop
    https://p5js.org/reference/#/p5/norm
    """
    return start + (stop-start) * value

def lerp(start, stop, amt):
    """
    Map a value between start and stop and return the corresponding position between 0 and 1
    https://p5js.org/reference/#/p5/lerp
    """
    return float(amt-start) / float(stop-start)
   

# set some constants
frames = 30      # number of frames
trail = 10       # number of outlines to draw behind our original
spokes = 1       # number of rotations to draw
myFontSize = 400 # the font size

# install the font or drag in the file to get the absolute path
myFont = 'Condor Variable'

# do i want to draw my helper dots?
# these visualize the sine curve and show me where i am in it
drawFrameDots = False

# okok let’s go

# loop through our frames
for frame in range(frames):
    # do some page setup
    # frame duration and background
    newPage(1000, 1000)
    frameDuration(1/10)
    rect(0, 0, width(), height())
    fill(1)
    # move to center
    translate(width()/2, height()/2)
    
    # loop through each "spoke in the wheel"
    for spoke in range(spokes):
        # set our alpha value, this will diminish
        a = 1
        
        # this section draws the frame dots
        # helps me remember where i am in the sine wave
        # it will only draw them if drawFrameDots is set to True
        if drawFrameDots:
            for i in range(frames):
                ix = i/frames * width() - width()/2
                ease = sin(2*pi * i/frames)
                iy = norm(ease, 0, width()/2)
                fill(1, 0, 0)
                if i == frame:
                    oval(ix-10, iy-10, 20, 20)
                else:
                    oval(ix-5, iy-5, 10, 10)
            
        # draw some text for our entire trail 
        for trailshape in range(0, -trail, -1):
            # get our easings
            # 2*pi = circumference
            # frame/frames is our progress through the animation
            # trailshape takes us “back in time”
            # sin wave begins and ends at the same place, nice for a loop
            # if we divide trailshape by a number, they will get closer than one frame apart
            ease = sin(2*pi * (frame-trailshape/3)/frames)
            easecos = sin(2*pi * (frame-trailshape/6)/frames)

            # set our display parameters
            stroke(1, 1, 1, a) 
            fill(None)
            # give our original spoke (horizontal text) a fill
            if spoke == 0:
                fill(1, .1)
            fontSize(myFontSize)
            lineHeight(myFontSize)
            font(myFont)
            # get the variations from the font and the min and max values to use
            # we can call these from listFontVariations() since they will change from font to font
            # it would be even cleaner to loop through these than to call them explicitly
            # but oh well
            myVariations = listFontVariations()
            wghtMin = myVariations['wght']['minValue']
            wghtMax = myVariations['wght']['maxValue']
            wdthMin = myVariations['wdth']['minValue']
            wdthMax = myVariations['wdth']['maxValue']
            italMin = myVariations['ital']['minValue']
            italMax = myVariations['ital']['maxValue']

            #oops i didn’t do this in class, but I wanna lerp my easing value here so it’s between 0 and 1 (otherwise it’s between -1 and 1, since the sine wave goes above AND below the starting point)
            print(ease)
            easeLerp = lerp(-1, 1, ease)
            easeCosLerp = lerp(-1, 1, easecos)
            
            # use the easing to get our axis values between the min and max
            wghtValue = norm(easeLerp, wghtMin, wghtMax)
            wdthValue = norm(easeCosLerp, wdthMin, wdthMax)
            italValue = norm(easeLerp, italMin, italMax)
            # feed those to the fontVariation() function
            fontVariations(wght=wghtValue, wdth=wdthValue, ital=italValue)
            # draw our text
            # use fontDescender() function to lower the text so the baseline 
            text('Hi!', (0, fontDescender()), align="center")
            # diminish our alpha channel for each trail
            a *= .9
        # for each spoke in our wheel, rotate one portion of a circle
        # divide 360 by the number of spokes to get the number of degrees to rotate
        rotate(360/spokes)
    
# save our image at the end
saveImage('~/desktop/hi.gif')