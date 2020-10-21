from random import randrange

chapterText = """Why don’t we just give everybody a promotion and call it a night – ‘Commander’? Mr. Crusher, ready a collision course with the Borg ship. The Enterprise computer system is controlled by three primary main processor cores, cross-linked with a redundant melacortz ramistat, fourteen kiloquad interface modules. Wouldn’t that bring about chaos? They were just sucked into space. Travel time to the nearest starbase? A lot of things can change in twelve years, Admiral. I’ll be sure to note that in my log. I can’t. As much as I care about you, my first duty is to the ship. Earl Grey tea, watercress sandwiches... and Bularian canapés? Are you up for promotion? Well, I’ll say this for him - he’s sure of himself. Fate. It protects fools, little children, and ships named “Enterprise.” The Federation’s gone; the Borg is everywhere! How long can two people talk about nothing? Your shields were failing, sir. I’m afraid I still don’t understand, sir. What? We’re not at all alike! Commander William Riker of the Starship Enterprise. Sure. You’d be surprised how far a hug goes with Geordi, or Worf. You bet I’m agitated! I may be surrounded by insanity, but I am not insane. Ensign Babyface! Now, how the hell do we defeat an enemy that knows us better than we know ourselves? Besides, you look good in a dress. Fear is the true enemy, the only enemy. What’s a knock-out like you doing in a computer-generated gin joint like this? Well, that’s certainly good to know. This should be interesting. Congratulations, you just destroyed the Enterprise. We have a saboteur aboard. Your head is not an artifact! Sorry, Data. Some days you get the bear, and some days the bear gets you. Flair is what marks the difference between artistry and mere competence. That might’ve been one of the shortest assignments in the history of Starfleet. I guess it’s better to be lucky than good. You enjoyed that. The unexpected is our normal routine. Not if I weaken first. Mr. Worf, you sound like a man who’s asking his friend if he can start dating his sister. You’re going to be an interesting companion, Mr. Data. Now we know what they mean by ‘advanced’ tactical training. Worf, It’s better than music. It’s jazz. Yes, absolutely, I do indeed concur, wholeheartedly! Yesterday I did not know how to eat gagh. The game’s not big enough unless it scares you a little. Damage report! I will obey your orders. I will serve this ship as First Officer. And in an attack against the Enterprise, I will die with this crew. But I will not break my oath of loyalty to Starfleet. Mr. Worf, you do remember how to fire phasers? About four years. I got tired of hearing how young I looked. Wait a minute - you’ve been declared dead. You can’t give orders around here. We could cause a diplomatic crisis. Take the ship into the Neutral Zone Talk about going nowhere fast. Fate protects fools, little children and ships named Enterprise. Some days you get the bear, and some days the bear gets you. Maybe if we felt any human loss as keenly as we feel one of those close to us, human history would be far less bloody. Computer, belay that order. And blowing into maximum warp speed, you appeared for an instant to be in two places at once. You did exactly what you had to do. You considered all your options, you tried every alternative and then you made the hard choice. When has justice ever been as simple as a rule book? Could someone survive inside a transporter buffer for 75 years? We know you’re dealing in stolen ore. But I wanna talk about the assassination attempt on Lieutenant Worf. Computer, lights up! Then maybe you should consider this: if anything happens to them, Starfleet is going to want a full investigation. A surprise party? Mr. Worf, I hate surprise parties. I would *never* do that to you. The look in your eyes, I recognize it. You used to have it for me. I am your worst nightmare! Is it my imagination, or have tempers become a little frayed on the ship lately? For an android with no feelings, he sure managed to evoke them in others. In all trust, there is the possibility for betrayal. Smooth as an android’s bottom, eh, Data? Maybe if we felt any human loss as keenly as we feel one of those close to us, human history would be far less bloody. Why don’t we just give everybody a promotion and call it a night - ‘Commander’? Mr. Crusher, ready a collision course with the Borg ship. The Enterprise computer system is controlled by three primary main processor cores, cross-linked with a redundant melacortz ramistat, fourteen kiloquad interface modules. Wouldn’t that bring about chaos? They were just sucked into space. Travel time to the nearest starbase? A lot of things can change in twelve years, Admiral. I’ll be sure to note that in my log. I can’t. As much as I care about you, my first duty is to the ship. Earl Grey tea, watercress sandwiches... and Bularian canapés? Are you up for promotion? Well, I’ll say this for him - he’s sure of himself. Fate. It protects fools, little children, and ships named “Enterprise.” The Federation’s gone; the Borg is everywhere! How long can two people talk about nothing? Your shields were failing, sir. I’m afraid I still don’t understand, sir. What? We’re not at all alike! Commander William Riker of the Starship Enterprise. Sure. You’d be surprised how far a hug goes with Geordi, or Worf. You bet I’m agitated! I may be surrounded by insanity, but I am not insane. Ensign Babyface! Now, how the hell do we defeat an enemy that knows us better than we know ourselves? Besides, you look good in a dress. Fear is the true enemy, the only enemy. What’s a knock-out like you doing in a computer-generated gin joint like this?"""

# this while loop will run as long as there is text in the chapterText varible
# we have to make sure to empty out this variable to avoid an infinite loop 😅
while chapterText:
    # create a new page
    newPage('Letter')
    
    # define a list of colors that we will use as a base, CMYK this time
    #           cyan       magenta   yellow    black      alpha 
    baseColor = [random(), random(), random(), random(), .3]
    
    # draw a solid background rectangle to start us out
    # use the * to unpack the list into its constituent parts
    cmykFill(*baseColor)
    rect(0, 0, width(), height())

    # we’re gonna draw some horizontal stripes
    # we will start with each band being the height of the page
    # then we will reduce this value each time to get a series of
    # rectangles
    bandHeight = height()

    # draw the background
    # this will be a series of 10 ever shrinking rectangle-like shapes
    # with a randomized curve for the top segment
    for row in range(10):
        
        # make a copy of our list
        # we make a copy becaues we don’t want
        # to modify the original baseColor list
        thisColor = baseColor.copy()
        # for this particular color, we will only change
        # one of the CMY values at random
        # by assigning it to a random value
        thisColor[randrange(0, 3)] = random()
        cmykFill(*thisColor)
    
        # now let’s make the shape by
        # making a BezierPath() object
        myPath = BezierPath()
        # begin by moving our “plotter” to (0, 0)
        myPath.moveTo((0, 0))
        # draw a straight line across the width of the page
        myPath.lineTo((width(), 0))
        # draw a straight line up the right side of the page to our bandHeight
        myPath.lineTo((width(), bandHeight))
        # draw a curve from the top right of the shape to the top left
        # the curveTo function takes three sets of coordinates
        # the first offcurve handle
        # the second offcurve handle
        # the oncurve point where we want to end up
        myPath.curveTo(
            (0, bandHeight+randrange(-200, 200)),
            (0, bandHeight+randrange(-200, 200)),
            (0, bandHeight)
            )
        # use this to join the last and first points 
        # (that’s the left side of the shape in this instance)
        myPath.closePath()
    
        # BezierPath() creates an object, but it doesn’t draw that object
        # to our canvas
        # for that we can use the drawPath() function
        drawPath(myPath)
    
        # if we didn’t want curves
        # we could have simply used 
        # the polygon function like this
        #polygon(
        #    (0, 0), 
        #    (width(), 0),
        #    (width(), bandHeight),
        #    (0, bandHeight)
        #)
    
        # every time we run the loop, we reduce the band height by 10%
        bandHeight -= height()/10
    
    # ok now we’re done with that background loop so
    # we dedent so we’re in the page loop

    # give ourselves an inch variable to make math easier
    inch = 72
    # define some outer and inner margins
    margin = 1 * inch
    innerMargin = .5 * inch
    
    # draw a white box starting at the lower left margin
    # and going to the upper right margin 
    # (this means the box will be the width and height of the page minus 2 margins)
    fill(1)
    rect(margin, margin, width()-margin*2, height()-margin*2)
    
    # make our fill black in prepartion to draw some text
    fill(0)
    # (you can get GimletText from Adobe Fonts if you want, or choose your own font!)
    font('GimletText-Regular', 13)
    # oooh we can turn on hyphenation too if we want
    hyphenation(True)

    # set variables for the dimensions of our text box
    # subtracting both the outer and inner margins from the page width and height
    textBoxWidth = width()-margin*2-innerMargin*2
    textBoxHeight = height()-margin*2-innerMargin*2
    textBoxOffset = margin+innerMargin
    
    # we’re going to use the textBox() function, which takes
    # the text to write
    # and a (x, y, w, h) rectangle to draw the text in
    
    # in addition, this function will RETURN the overflow text
    # so we will capture that overflow by redefining chapterText
    # each time
    chapterText = textBox(chapterText, (textBoxOffset, textBoxOffset, textBoxWidth, textBoxHeight))
    # if you want, you can add the optional argument 
    # align="justified"
    # to textBox() to get justified text!

    # let’s print chapter text each time, just so we can see the whittling down 
    # of the variable’s contents
    print(chapterText)

# save the image as a PDF
saveImage('~/desktop/myFancyBook.pdf')