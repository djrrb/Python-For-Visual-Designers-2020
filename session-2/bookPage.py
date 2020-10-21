from random import randrange

chapterText = """Why don't we just give everybody a promotion and call it a night - 'Commander'? Mr. Crusher, ready a collision course with the Borg ship. The Enterprise computer system is controlled by three primary main processor cores, cross-linked with a redundant melacortz ramistat, fourteen kiloquad interface modules. Wouldn't that bring about chaos? They were just sucked into space. Travel time to the nearest starbase? A lot of things can change in twelve years, Admiral. I'll be sure to note that in my log. I can't. As much as I care about you, my first duty is to the ship. Earl Grey tea, watercress sandwiches... and Bularian canapés? Are you up for promotion? Well, I'll say this for him - he's sure of himself. Fate. It protects fools, little children, and ships named "Enterprise." The Federation's gone; the Borg is everywhere! How long can two people talk about nothing? Your shields were failing, sir. I'm afraid I still don't understand, sir. What? We're not at all alike! Commander William Riker of the Starship Enterprise. Sure. You'd be surprised how far a hug goes with Geordi, or Worf. You bet I'm agitated! I may be surrounded by insanity, but I am not insane. Ensign Babyface! Now, how the hell do we defeat an enemy that knows us better than we know ourselves? Besides, you look good in a dress. Fear is the true enemy, the only enemy. What's a knock-out like you doing in a computer-generated gin joint like this? Well, that's certainly good to know. This should be interesting. Congratulations - you just destroyed the Enterprise. We have a saboteur aboard. Your head is not an artifact! Sorry, Data. Some days you get the bear, and some days the bear gets you. Flair is what marks the difference between artistry and mere competence. That might've been one of the shortest assignments in the history of Starfleet. I guess it's better to be lucky than good. You enjoyed that. The unexpected is our normal routine. Not if I weaken first. Mr. Worf, you sound like a man who's asking his friend if he can start dating his sister. You're going to be an interesting companion, Mr. Data. Now we know what they mean by 'advanced' tactical training. Worf, It's better than music. It's jazz. Yes, absolutely, I do indeed concur, wholeheartedly! Yesterday I did not know how to eat gagh. The game's not big enough unless it scares you a little. Damage report! I will obey your orders. I will serve this ship as First Officer. And in an attack against the Enterprise, I will die with this crew. But I will not break my oath of loyalty to Starfleet. Mr. Worf, you do remember how to fire phasers? About four years. I got tired of hearing how young I looked. Wait a minute - you've been declared dead. You can't give orders around here. We could cause a diplomatic crisis. Take the ship into the Neutral Zone Talk about going nowhere fast. Fate protects fools, little children and ships named Enterprise. Some days you get the bear, and some days the bear gets you. Maybe if we felt any human loss as keenly as we feel one of those close to us, human history would be far less bloody. Computer, belay that order. And blowing into maximum warp speed, you appeared for an instant to be in two places at once. You did exactly what you had to do. You considered all your options, you tried every alternative and then you made the hard choice. When has justice ever been as simple as a rule book? Could someone survive inside a transporter buffer for 75 years? We know you're dealing in stolen ore. But I wanna talk about the assassination attempt on Lieutenant Worf. Computer, lights up! Then maybe you should consider this: if anything happens to them, Starfleet is going to want a full investigation. A surprise party? Mr. Worf, I hate surprise parties. I would *never* do that to you. The look in your eyes, I recognize it. You used to have it for me. I am your worst nightmare! Is it my imagination, or have tempers become a little frayed on the ship lately? For an android with no feelings, he sure managed to evoke them in others. In all trust, there is the possibility for betrayal. Smooth as an android's bottom, eh, Data? Maybe if we felt any human loss as keenly as we feel one of those close to us, human history would be far less bloody."""

newPage('Letter')
#            cyan      magenta     yellow     black  alpha 
baseColor = [random(), random(), random(), random(), .3]

bandHeight = height()

# draw the background
for row in range(10):
    thisColor = baseColor.copy()
    thisColor[randrange(0, 3)] = random()
    cmykFill(*thisColor)
    
    myPath = BezierPath()
    myPath.moveTo((0, 0))
    myPath.lineTo((width(), 0))
    myPath.lineTo((width(), bandHeight))
    myPath.curveTo(
        (0, bandHeight+randrange(-100, 100)),
        (0, bandHeight+randrange(-100, 100)),
        (0, bandHeight)
        )
    myPath.closePath()
    
    drawPath(myPath)
    
    #polygon(
    #    (0, 0), 
    #    (width(), 0),
    #    (width(), bandHeight),
    #    (0, bandHeight)
    #)
    
    bandHeight -= height()/10
    
inch = 72
margin = 1 * inch
fill(1)
rect(margin, margin, width()-margin*2, height()-margin*2)
fill(0)
font('GimletText-Regular')
openTypeFeatures(smcp=True)
fontSize(100)
text('AVALTED', (margin, margin))