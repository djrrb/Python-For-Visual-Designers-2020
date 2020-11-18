fs = FormattedString('hello', font="MyFont", fontSize=200)
# will this work
fs.appendGlyph('nine')
text(fs, (100, 100))