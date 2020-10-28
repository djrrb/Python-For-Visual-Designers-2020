# imagePixelColor() demo
# https://www.drawbot.com/content/image/imageProperties.html?highlight=imagePixelColor#drawBot.imagePixelColor

# import our random library, which we will use to choose letters at random
import random

# make a list of letters that we will draw from
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# make an image object for our image
im = ImageObject('https://github.com/djrrb/Python-For-Visual-Designers-2020/blob/main/session-3/black-raspberries.jpg?raw=true')

# on the first page, draw our image
# use the imageObject’s size as the canvas size
newPage(*im.size())
image(im, (0, 0))

# make a new page
newPage(*im.size())

# draw a black background
rect(0, 0, width(), height())

# do our typical x, y loop
for y in range(0, int(height()), 10):
    for x in range(0, int(width()), 10):
        
        # use imagePixelColor() to query the image object and give us back the color of the pixel at (x, y)
        # this is just like using the eyedropper tool
        myColor = imagePixelColor(im, (x, y)) 
        
        # set the fill color to that pixel color
        fill(*myColor)
        
        # change the font and font size
        font('Verdana-Bold')
        fontSize(13.5)
        
        # draw a random letter from our alphabet at x, y
        text(random.choice(alphabet), (x, y))