# https://www.drawbot.com/content/image/imageObject.html

# instantiate an image object
im = ImageObject('black-raspberries.jpg')
# get our width height
# unpack the (x, y) tuple
w, h = im.size()

######
######
######

newPage(w, h)
# draw the image as it came from the file
image(im, (0, 0))

######
######
######

# now make a new page
newPage(w, h)
# now add some filters to the image
# how about a vignette to fade the edges
im.vignette(50, 1)
# and a sepia tone
im.sepiaTone(.8)
# now draw the image as it stands
image(im, (0, 0))

######
######
######

# let’s keep going and try a couple more
newPage(w, h)

im.zoomBlur(center=(width()/2, height()/2), amount=15)
# this filter changes the size of the image
# so let’s just put the image in the center
translate(width()/2, height()/2)
image(im, (-im.size()[0]/2, -im.size()[1]/2))

######
######
######

newPage(w, h)
# ok too much already let’s clear those filters
im.clearFilters()
# oooh how about a halftone!?
im.dotScreen(center=(width()/2, height()/2), angle=30, width=20, sharpness=0)
image(im, (0, 0))


######
######
######

newPage(w, h)
# clear filters again
im.clearFilters()
# ooooh kaleidoscope filter!?!? what does that do?
im.kaleidoscope(0)
# changes the image size so let’s draw it from the center again
# and try to make it fit
imw, imh = im.size()
translate(width()/2, height()/2)
scale(.7)
image(im, (-imw/2, -imh/2))

