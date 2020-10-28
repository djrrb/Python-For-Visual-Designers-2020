# world’s worst alphabet book
margin = 50

# make a new page for each letter of the alphabet
for myLetter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    newPage('Letter')

    # draw the background
    fill(random(), random(), random())
    rect(0, 0, width(), height())

    fill(0)
    with savedState():
        # determine the width of the content
        contentWidth = width()-margin*2
        contentHeight = height()-margin*2
        # set our origin to the margins so we don’t have to worry
        translate(margin, margin)
        # draw our content area in black 
        fill(0)
        rect(0, 0, contentWidth, contentHeight)
        # set the font and stuff
        font('Comic Sans MS')
        fontSize(400)
        # get the size of the text we are drawing
        textWidth, textHeight = textSize(myLetter)
        # draw a bunch of randomly positioned letters
        for i in range(10):
            # random color
            fill(random(), random(), random())
            # draw it starting anywhere from the left margin (now 0, 0) to the right or top of the content minus the width or cap height
            text(
                    myLetter, 
                    (
                    randint(0, int(contentWidth-textWidth)),
                    randint(0, int(contentHeight-fontCapHeight()))
                    )
                )
    # OK now we’ve left the savedState()
    # that means we are back to the bottom corner of the page
    # that means no more comic sans
    # that means mo more random fill
    
    # let’s draw a page number
    text(str(pageCount()), (margin, margin/2))