# use textSize() and fontXHeight() to center a text block

# what are we typing
myString = 'Hello there!\nThis is a wedding invitation\nso the text is centered!\n\nVery Fancy!'

# set our font parameters
font("Verdana")
fontSize(100)

margin = 25

fill(0, 1, 0)
rect(margin, margin, width()-margin*2, height()-margin*2 )
fill(0)
textBox(myString, 
    (margin, margin, width()-margin*2, height()-margin*2 ),
    align="center"
    )