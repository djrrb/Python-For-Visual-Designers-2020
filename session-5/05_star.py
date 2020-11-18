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
   
def star(x, y, n, r1, r2):
    pts = []
    for i in range(n * 2):
        a = i * pi / n
        r = r2 if i % 2 else r1
        pts.append((x + r * sin(a), y + r * cos(a)))
    polygon(*pts) 


frames = 30
trail = 10
spokes = 7


for frame in range(frames):
    newPage(1000, 1000)
    frameDuration(1/15)
    rect(0, 0, width(), height())
    fill(1)
    # move to center
    translate(width()/2, height()/2)
    
    
    for spoke in range(spokes):
        d = 100
        a = 1
        for trailshape in range(-trail, 0):
            ease = sin(2*pi * (frame-trailshape/4)/frames)
            x = 0
            y = norm(ease, 0, width()/2)
            print(ease, y) 
            # define diameter

            stroke(1, 1, 1, a)
            fill(None)
            # draw my oval
            #oval(x-d/2, y-d/2, d, d)
            star(x, y, 7, d, d/2)
            a *= .9
            d *= .9
        rotate(360/spokes)
    
saveImage('~/desktop/movingdot.gif')