frames = 30


for frame in range(frames):
    newPage(1000, 1000)
    rect(0, 0, width(), height())
    fill(1)
    # move to center
    translate(width()/2, height()/2)
    for step in range(frames):
        x = -width()/2 + (step/frames) * width()
        y = 0
        
        # define diameter
        if frame == step:
            d = 100
        else:
            d = 10
        
        # draw my oval
        oval(x-d/2, y-d/2, d, d)
        
    
saveImage('~/desktop/movingdot.gif')