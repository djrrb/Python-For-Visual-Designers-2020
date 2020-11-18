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
trail = 10


for frame in range(frames):
    newPage(1000, 1000)
    frameDuration(1/15)
    rect(0, 0, width(), height())
    fill(1)
    # move to center
    translate(width()/2, height()/2)
    d = 100
    a = 1
    for trailshape in range(-trail, 0):
        ease = sin(2*pi * (frame-trailshape/2)/frames)
        x = 0
        y = norm(ease, 0, width()/2)
        print(ease, y) 
        # define diameter

        fill(1, 1, 1, a)
        # draw my oval
        oval(x-d/2, y-d/2, d, d)
        a *= .9
        d *= .9
        
    
saveImage('~/desktop/movingdot.gif')