import random

minPointValue = 30
maxPointValue = width()-30

minPointCount = 3
maxPointCount = 40

minShapeCount = 15
maxShapeCount = 35

HEIGHT = 1000
WIDTH = 1000

shapeCount = random.randrange(minShapeCount, maxShapeCount)
#print 'number of polygons:', shapeCount

alphaStart = random.uniform(.8, 1)
alphaMin = random.uniform(0, .2)
alphaIncrement = (alphaStart - alphaMin) / shapeCount

im = ImageObject()

with im:

    for tick in range(0, shapeCount):
    
        #color
        r = random.random()
        g = random.random()
        b = random.random()
        a = alphaStart - (alphaIncrement * tick)
        fill(r, g, b, a)

        pointCount = random.randrange(minPointCount, maxPointCount)
        args = []
        for pointIndex in range(0, pointCount):
            x = random.randrange(minPointValue, maxPointValue)
            y = random.randrange(minPointValue, maxPointValue)
            args.append((x, y))

        polygon(*args)

#im.perspectiveTransform((0, 10), (0, 10), (0, 0), (10, 0))

newPage(1000, 1000)
image(im, (0, 0))
newPage(1000, 1000)
im.QRCodeGenerator((1000, 1000), message='Sup', correctionLevel=1)

image(im, (0, 0))