def star(x, y, n, r1, r2):
    pts = []
    for i in range(n * 2):
        a = i * pi / n
        r = r2 if i % 2 else r1
        pts.append((x + r * sin(a), y + r * cos(a)))
    polygon(*pts)

def lerp(start, stop, amt):
	return float(amt-start) / float(stop-start)

def norm(value, start, stop):
	return start + (stop-start) * value

frames = 60
rotations = 7

step = width()/frames
for frame in range(frames):
    newPage(1000, 1000)
    frameDuration(1/15)
    rect(0, 0, width(), height())
    translate(width()/2, height()/2)
    for drawFrame in range(frames):
        x = drawFrame * step
        x = drawFrame * step
        ease = sin(2*pi*drawFrame/frames)
        y = norm(ease, 0, height()/2)
        d = 10
        fill(1, 0, 1, .5)
        #oval(-width()/2+x-d/2, y-d/2, d, d)
    with savedState():
        for rotation in range(rotations):
            a = .1
            d = 150
            for trail in range(-9, 1, 1):
                ease = sin(2*pi*(frame+trail/2)/frames)
                y = norm(ease, 0, height()/3)
                x = 0
                stroke(1, 1, 1, a)
                fill(None)
                #oval(x-d/2, y-d/2, d, d)
                if trail == 0:
                    fill(1,1,1,a)
                star(x, y, rotations, d/3, d)
                a += .1
                d *= .9
            rotate(360/rotations)
    
saveImage('~/desktop/bounce.gif')