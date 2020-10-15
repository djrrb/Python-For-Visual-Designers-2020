# This script uses some stuff with images that we haven’t learned yet

# it is in response to a question from Steena about recovering randomly-generated colors, which is only possible if we save a PDF and eyedrop it 

# this script will take an image or PDF file
# (shown on the left)
# and replicate the colors in a new grid
# (shown on the right)


# it will only work if the imagePath points to a file
# on your local system
imagePath = 'grid-to-sample.pdf'

# create an image object
# this provides us with an interface with which we can interact with the image using drawbot
im = ImageObject(imagePath)

# how big should the eyedropper dot be that we draw
d = 5

# draw this twice the width of the original
# old on the left
# new on the right
newPage(2000, 1000)
image(im, (0, 0))

# set the size of the grid that we want to measure
rows = cols = 10
gridWidth = gridHeight = 100
x = y = 0

# loop through the rows and columns
for row in range(rows):
    for col in range(cols):
        # let’s play it safe and sample from the center of the grid, rather than the bottom left corner
        # we get the center by adding half the gridWidth to X and Y
        centerX = x + gridWidth/2
        centerY = y + gridWidth/2
        # Draw a red dot to show where we are eye dropping from
        # we don’t have to do this but I like to see what I’m sampling
        fill(1, 0, 0)
        oval(centerX-d/2, centerY-d/2, d, d)
        # use imagePixelColor() to eyedrop from the PDF
        # https://www.drawbot.com/content/image/imageProperties.html#drawBot.imagePixelColor
        color = imagePixelColor(im, (centerX, centerY))
        # print the row, column, and color
        print(row, col, color)
        # prove that we got the shape by setting it as the fill color and replicating it 1000 units to the right
        fill(*color)
        oval(x+1000, y, gridWidth, gridHeight)
        # increment the column
        x += gridWidth
    # increment the row
    x -= gridWidth*cols
    y += gridHeight
    
    