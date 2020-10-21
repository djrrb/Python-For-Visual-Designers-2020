x = 0
y = 0
newPage(1000, 50000)
for fontName in installedFonts():
    font(fontName)
    text(fontName, (x, y))
    y += 20