m = 72

newPage('Letter')

with savedState():
    translate(m, m)
    contentWidth = width()-m*2
    contentHeight = height()-m*2

    rect(0, 0, contentWidth, contentHeight)
    fill(1)
    fontSize(50)
    text('Hello', (0, 0))

    translate(100, 100)
    text('Goodbye', (0, 0))

with savedState():
    pageNumberText = 'Page ' + str(pageCount())
    translate(width()-m, height()-m+20)
    text(pageNumberText, (0, 0), align="right")
    

