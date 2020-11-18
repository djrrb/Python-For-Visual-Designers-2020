import calendar
import colorsys
from datetime import date

def norm(value, start, stop):
    """
    Map a value between 0 and 1 and return the corresponding position between start and stop
    https://p5js.org/reference/#/p5/norm
    """
    return start + (stop-start) * value

def lerp(start, stop, amt):
    """
    Map a value between start and stop and return the corresponding position between 0 and 1
    https://p5js.org/reference/#/p5/lerp
    """
    return float(amt-start) / float(stop-start)
   

# some constants
# the gray we want to use
g = .9

inch = 72
margin = inch/2
im = 10             # internal margin
titleHeight = 40
headerHeight = 30

# instead of hardcodin the year, let’s make a slider
# this is a silly use case since these are much better controlled numerically but oh well i wanted to show it to you anyway
# see more at https://www.drawbot.com/content/variables.html
Variable([
    dict(name="year", ui="Slider",
            args=dict(
                value=date.today().year+1,
                minValue=date.today().year-100,
                maxValue=date.today().year+100)),
    dict(name="pageWidth", ui="Slider",
            args=dict(
                value=sizes('A2Landscape')[0],
                minValue=72,
                maxValue=1000)),
    dict(name="pageHeight", ui="Slider",
            args=dict(
                value=sizes('A2Landscape')[1],
                minValue=72,
                maxValue=1000)),
    ], globals())

# convert the results of our slider to a rounded integer
year = int(round(year))

# if we did want to hardcode the year, we could uncomment the following line
#year = 2021

# do we want the calendar to start on sunday or monday?
startOnSunday = True

# let’s cache some font settings so we can call them up easily
def setFont():
    font('Rhody Variable')
    # because this is a function and we are executing it each time
    # we could get a random font each time this function is run
    # by uncommenting the following two lines
    #from random import choice
    #font(choice(installedFonts()))
    fontSize(60)
    lineHeight(60)
    fontVariations(wght=900)

def getHeaderFont():
    font('InputSansNarrow-Light')
    fontSize(20)
    tracking(1)


# Okay let’s make this thing

# loop through months and make a new page for each
for month in range(0, 12):
    # we actually don’t want to start with the 0th month so...
    month += 1
    # get our calendar object from the built-in library
    # have the calendar start on sunday
    if startOnSunday:
        calendar.setfirstweekday(6)
    # get our calendar
    # this is a list of week rows, and each week row is a list of days
    thisCalendar = calendar.monthcalendar(year, month)
    # make a new page
    newPage(int(pageWidth), int(pageHeight))
    frameDuration(1/2)
    fill(1)
    rect(0, 0, width(), height())
    
    # get the size of the day grid itself
    # subtract the margins, header, etc from full page dimensions
    contentWidth = width()-margin*2
    contentHeight = height()-margin*2-titleHeight-headerHeight

    # get the dimensions of each box within the day grid
    # the height is divided by the number of rows
    boxH = contentHeight/len(thisCalendar)
    # the width is divided by the number of columns
    boxW = contentWidth/len(thisCalendar[0])
    
    # draw the title
    with savedState():
        translate(width()/2, height()-margin-titleHeight)
        monthname = calendar.month_name[month]
        setFont()
        fill(0)
        text(str(monthname + ' ' +str(year)), (0, -fontDescender()), align="center")
 
    # move to the top of the content
    translate(margin, margin+contentHeight)
    
    # do the weekday header
    with savedState():
        getHeaderFont()
        # get a list of the days of the week (0-6)
        dayOfWeekCount = len(thisCalendar[0])
        daysOfWeek = list(range(dayOfWeekCount))
        if startOnSunday:
            # ugh this is a tricky thing
            # because we want to start on sunday, we have to move the last item of this list to the front
            daysOfWeek = [daysOfWeek[-1]] + daysOfWeek[:-1]
            
        # draw our headers
        for x in daysOfWeek:
            # get the day name from the calendar module
            dayName = calendar.day_name[x]
            # make a background rectangle
            fill(1)
            stroke(g)
            strokeWidth(3)
            rect(0, 0, boxW, headerHeight)
            # draw the text
            fill(0)
            stroke(None)
            text(dayName.upper(), (boxW/2, im), align="center")
            # move to the next column
            translate(boxW)
            
    # now draw the day boxes
    # since the boxes draw from the bottom left corner
    # move our "cursor" down one box height before we begin our loop
    translate(0, -boxH)

    # loop through the rows
    for y in range(len(thisCalendar)):
        # now loop through the columns and save where we were
        with savedState():
            for x in range(len(thisCalendar[0])):
                # get the value for the particular day by selecting from the list of lists
                # this will be 0 if there’s no day on this part of the grid
                dayValue = thisCalendar[y][x]
                # if there isn’t a day for this slot, make it gray
                if dayValue == 0:
                    fill(g)
                else:
                    # otherwise, interpolate our progress through the month
                    monthProgress = lerp(0, 31, dayValue)
                    # and use that progress as the hue value so we have a nice rainbow-type-thing
                    fill(*colorsys.hsv_to_rgb(monthProgress/2, .3, .9))
                rect(0, 0, boxW, boxH)
                # draw our text
                fill(0)
                stroke(None)
                setFont()
                # only draw text if there’s a number other than 0
                # the text box allows us to set some internal margins so the
                # text doesn’t hit the border of the frame
                if dayValue != 0:
                    textBox(str(dayValue), (im, im, boxW-im*2, boxH-im*2))
                # move to the next column
                translate(boxW)
        # exiting the saved state moves us back to the left margin
        # now we move down a row 
        translate(0, -boxH)
        
#saveImage('~/desktop/calendar.pdf')