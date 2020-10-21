from random import choice
margin = inch = 72

fs = FormattedString(fontSize=12, lineHeight=20)
for fontName in installedFonts():
    # exclude any fonts whose first character is a period
    # != means not equal to
    if fontName[0] != '.':
        # give it the fontName and a space as text
        # set the font
        # and set the fill to a random greenish color
        fs.append(
            fontName + ' ', 
            font=fontName, 
            fill=(0, random(), 0, 1)
        )
       
# now we have built up this really long FormattedString
print(fs)

# do our while loop to keep making pages till its printed
while fs:
    # make a new page
    newPage('A2Landscape')
    # set the textBox overflow to the fs variable
    
    fs = textBox(fs, (margin, margin, width()-margin*2, height()-margin*2))
    
    # oh oh how about a little bonus
    # let’s also draw a page number at the bottom right corner of each page

    # get the current number of pages using the pageCount() function
    # we have to use str() to convert it to a string
    # since we will treat it as text, not an integer
    pageNumberText = 'Page ' + str(pageCount())
    
    # choose a random font from the list
    # this uses the choice() function, which
    # imported from the random library on the first line
    pageNumberFont = choice(installedFonts())
    
    # set the font properties
    font(pageNumberFont)
    fill(0)
    fontSize(12)
    lineHeight(12)
    
    # put it in a text box
    # I’ve lowered this text box 12pt into the margin, and made it 12pt tall
    # this way it won’t hit the other text box
    # i’ve also used the optional align argument to
    # align the page number to the right
    textBox(pageNumberText, (margin, margin-12, width()-margin*2, 12), align="right")
    