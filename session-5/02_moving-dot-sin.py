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
    


frames = 30


for frame in range(frames):
    newPage(1000, 1000)
    frameDuration(1/15)
    rect(0, 0, width(), height())
    fill(1)
    # move to center
    translate(width()/2, height()/2)
    for step in range(frames):
        ease = sin(2*pi * step/frames)
        x = -width()/2 + (step/frames) * width()

        y = norm(ease, 0, width()/2)
        print(ease, y) 
        # define diameter
        if frame == step:
            d = 100
        else:
            d = 10
        
        # draw my oval
        oval(x-d/2, y-d/2, d, d)
        
    
saveImage('~/desktop/movingdot.gif')