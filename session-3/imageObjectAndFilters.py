# https://www.drawbot.com/content/image/imageObject.html

# instantiate an image object
im = ImageObject('black-raspberries.jpg')
# get our width height
# unpack the (x, y) tuple
w, h = im.size()

# make our page twice the height
newPage(w, h)

# draw the image as it came from the file
image(im, (0, 0))

# now make a new page
newPage(w, h)
# now add some filters to the image
# how about a vignette to fade the edges
im.vignette(50, 1)
# and a sepia tone
im.sepiaTone(.8)

# now draw the image as it stands
image(im, (0, 0))


# let’s keep going and try a couple more
newPage(w, h)

