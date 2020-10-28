# use textSize() and fontXHeight() to center a text block

# what are we typing
myString = 'Hello there!'

# set our font parameters
font("Verdana")
fontSize(100)

# get the text dimensions
textWidth, textHeight = textSize(myString)

# get the difference between the text width and the page width
# if we divide that in 2, the margin will be equal on both sides
widthDifference = width()-textWidth
xoffset = widthDifference/2

# do the same thing with the height, but calculate it based on the xHeight
heightDifference = height()-fontXHeight()
yoffset = heightDifference/2

# draw guidelines to show the box we are centering
# do this within a saved state so that these formatting options aren’t saved
with savedState():
    # set red stroke
    stroke(1, 0, 0)
    # left side
    line((xoffset, 0), (xoffset, height()))
    # right side
    line((width()-xoffset, 0), (width()-xoffset, height()))
    # text baseline
    line((0, yoffset), (width(), yoffset))
    # text x-height
    line((0, height()-yoffset), (width(), height()-yoffset))
    
# draw our text
text(myString, (xoffset, yoffset))