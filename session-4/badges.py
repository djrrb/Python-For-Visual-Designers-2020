import csv
csvPath = 'Fantasy Conference  - Sheet1.csv'

with open(csvPath, 'r', encoding="utf-8") as csvFile:
    #fileText = csvFile.read()
    # mehhh let’s not split this up as a string
    #lines = fileText.split('\n')
    #for line in lines:
    #    columns = line.split(',')
    #    print(columns[2])
    
    inch = 72
    fullWidth = 8.5
    fullHeight = 11
    
    reader = csv.reader(csvFile)
    for tick, row in enumerate(reader):
        if tick == 0:
            continue
        name, affiliation, role = row
        role = role.title()
        print(role)
        newPage(fullWidth*inch/2, fullHeight*inch/4)
        margin = .25*inch
        contentWidth = width()-margin*2
        contentHeight = height()-margin*2
        nameWidth = contentWidth - margin*2
        nameHeight = contentHeight - margin*2
        translate(margin, margin)
        if role == 'Attendee':
            fill(0, 1, 0)
        elif role == 'Speaker':
            fill(0, 0, 1)
        else:
            fill(1, 0, 0)
        rect(0, 0, contentWidth, contentHeight)
        fontSize(50)
        fill(1)
        words = name.split(' ')
        
        lines = []
        for word in words:
            if len(word) > 3:
                lines.append(word)
            else:
                lines[-1] += ' ' + word
                
        print(words, lines)
        
        fs = FormattedString()
        for word in lines:
            fontSize(1)
            tw, th = textSize(word)
            
            myFontSize = nameWidth / tw 
            if myFontSize > 50:
                myFontSize = 50
            
            fontSize(myFontSize)
            fs.append(word+'\n',
                fontSize=myFontSize,
                lineHeight=myFontSize,
                align="center",
                font='Georgia',
        
                fill=(random(), random(), random())
            )
        
        
        tw, th = textSize(fs, width=nameWidth)
        yoffset = (nameHeight - th)/2
        
        #fill(1, 0, 0)
        #rect(margin, margin*2, nameWidth, nameHeight-yoffset)
        if affiliation:
            bottomMargin = margin*2
        else:
            bottomMargin = margin
        textBox(fs, (margin, bottomMargin, nameWidth, nameHeight-yoffset))

        # affiliation saved state
        with savedState():
            fill(1)
            fontSize(10)
            translate(contentWidth/2, margin)
            #oval(-5, -5, 10, 10)
            stroke(1)
            if affiliation:
                line((-nameWidth/2, margin), (nameWidth/2, margin))
            stroke(None)
            text(affiliation, (0, 0), align="center")
        