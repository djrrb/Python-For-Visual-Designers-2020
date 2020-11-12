# Python For Visual Designers

* Type@Cooper Public Workshop
* _Term:_ Fall 2020
* _Dates:_ Tuesdays 7–9pm ET, October 13–27 and November 10–17
* _Instructor:_ [David Jonathan Ross](https://djr.com)
* _Office Hours:_ [Book on Calendly](http://calendly.com/djrrb/office-hours) or get in touch

## Course Description

Designers use tools to help us get our work done, but we rarely consider how much these tools can box us in to certain processes and solutions in our work. Creating our own tools can lead us down new and unexpected avenues in our designs: some of the best visual ideas can come about by setting up some boundaries — a color palette, a typeface or two — and then running wild within the system. And working out a system in code is a great way to explore these ideas: computers love repetition and can quickly make hundreds of variations on a theme, and mistakes in the code can result in something that often looks better than what was originally intended.

With no programming experience necessary, workshop participants will learn the basics of the Python programming language while working in the free DrawBot application for MacOS. A quick sketch made with code in DrawBot can be saved as a PDF as a starting point to be finished later in Illustrator, or, with a little bit more work in the code editor, an entire book, magazine or animation can be built without even launching Illustrator or InDesign.

Using the fundamentals of the Python programming language, students will sketch to create vector art with code and use the basic principles of design to turn their sketches into PDF zines and animated gifs.

### Required Materials

* A computer with macOS 10.9 (Mavericks) or newer
* A fast enough internet connection for video calls

### Software

* [Drawbot](https://www.drawbot.com)
* A coding font of your choice!

### Course structure

Most of class time will be spent coding together in the Drawbot app. In between courses, students are encouraged to practice the skills learned during class and experiment with them. 

Between the third and fifth class sessions, each student will be asked to work on a few spreads that we will turn into a collective zine.

Beyond the nuts and bolts of Python programming, I hope students use this opportunity to step back and consider how Python/Drawbot might affect their relationship with their tools. I will provide Optional readings and links for students that explore this topic at their leisure, even though they may not relate directly to the course materials.

### Credits

This Type@Cooper course was originated by [Andy Clymer](http://www.andyclymer.com), and its structure and content owe much to his work. 

## Course Outline
| Session | Date | Subject |
| ---- | ---- | -------------- | 
| 1   | October 13 | [**Shapes and Loops**](#Session-1-Shapes-and-Loops) | 
| 2   | October 20 | [**Colors and Text**](#Session-2-Colors-and-Text) | 
| 3   | October 27 | [**Canvas and Images**](#Session-3-Paths-and-Images) | 
| | | _Daylight savings ends, move back 1 hour_ |
|   |  _November 3_ | _Optional drop-in class_ | 
| 4   | November 10 | [**Layouts**](#Session-4-Layouts) |
| 5   | November 17 | [**Animation**](#Session-5-Animation)|

## Sessions

### Session 1: Shapes and Loops

* Introductions
* The Drawbot interface
* Keyboard shortcuts
* [Hello world](session-1/1-helloWorld.py)
* [Math](session-1/2-math.py)
* Strings
* Comments
* [Variables](session-1/3-variables.py)
* Drawbot primitives ([docs](https://www.drawbot.com/content/shapes/primitives.html))
* Loops
* Conditions

#### Session links
* [**Session 1 scripts**](/session-1)
* [**Recorded demo**](https://vimeo.com/468553019/111e5ae886)

#### Optional readings
* [The Zen of Python](https://www.python.org/dev/peps/pep-0020/#easter-egg)
* [Connections TV series](https://archive.org/details/ConnectionsByJamesBurke), also some epsiodes [on YouTube](https://www.youtube.com/playlist?list=PLw7aVsjFLyMmkEqHami9AHGmc3x3-s3xa)
* [Esoteric programming languages](https://esolangs.org/wiki/Esoteric_programming_language)
	* [LOLCODE](https://esolangs.org/wiki/LOLCODE)
	* [Folders](http://danieltemkin.com/Esolangs/Folders/)
	* [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck)
* [Drawbot icon by Andy Clymer](https://www.drawbot.com/content/drawBotIcon.html)
* [Merriweather Font](https://fonts.google.com/specimen/Merriweather), by [Eben Sorkin](http://sorkintype.com) who generously donated his porch so we could have class

 

### Session 2: Colors and Text

* _Review_
* _Show & Tell_
* Lists
* Booleans
* Canvas
  * Pages
  * Graphics State ([docs]((https://www.drawbot.com/content/canvas/state.html)))
  * Saving ([docs](https://www.drawbot.com/content/canvas/saveImage.html))
* Functions
* Text ([docs](https://www.drawbot.com/content/text/drawingText.html))
* Formatted Strings ([docs](https://www.drawbot.com/content/text/formattedString.html))
* Color ([docs](https://www.drawbot.com/content/color.html))
* colorsys ([docs](https://docs.python.org/3/library/colorsys.html))

#### Session links
* [**Scripts**](/session-2)
* [**Recorded demo**](https://vimeo.com/470438779/7b576c248d)

#### Optional readings
* [Duck Typing](https://www.pythonmorsels.com/topics/duck-typing/)
* [Python Object Types](https://www.oreilly.com/library/view/learning-python-3rd/9780596513986/ch04.html)
* [Typographische Monatsblätter Research Archive](http://www.tm-research-archive.ch)
* [Nancy White](https://www.artsy.net/artist/nancy-white)
* [Python colorsys module](https://docs.python.org/3/library/colorsys.html)


### Session 3: Paths and Images

* _Review_
* _Show & Tell_
* Paths ([docs](https://www.drawbot.com/content/shapes/bezierPath.html))
* Color ([docs](https://www.drawbot.com/content/color.html))
* Image Object ([docs](https://www.drawbot.com/content/image/imageObject.html))

#### Session links
* [**Scripts**](/session-3)
* [**Session Recording, Part 1**](https://vimeo.com/473111438) (`translate()`, `rotate()`, and `scale()`)
* [**Session Recording, Part 2**](https://vimeo.com/473126307) (`savedState()`, `ImageObject()`)



#### Optional readings
* [Vera Molnar](http://www.veramolnar.com)
* [@beesandbombs](https://twitter.com/beesandbombs)
* [Daily Drawbot](https://dailydrawbot.tumblr.com)
* [Maurice Meilleur](https://mauricemeilleur.net/munari_peano)
* [Drawbot Forum Code Snippets](https://forum.drawbot.com/category/8/code-snippets)
* [Drawbot American Flag](https://github.com/djrrb/OldGlory/blob/master/oldGlory.py)

### Session 4: Layouts

* _Review_
* _Show & Tell_
* Installing Python Packages
* Importing and Parsing Data


#### Session links
* [**Scripts**](/session-4)
* [**Session recording**](https://vimeo.com/478115143/b29a9471d3)

#### Optional readings
* See #random channel for code snippets

### Session 5: Animation

* _Review_
* _Show & Tell_
* Animation techniques
* Easing
* Saving and exporting


#### Session links
* Scripts _(TBA)_
* Session recording _(TBA)_

#### Optional readings
* _(TBA)_




## Additional resources

### Drawbot resources
* [Drawbot Documentation](https://www.drawbot.com/#)
* [Drawbot on GitHub](https://github.com/typemytype/drawbot)
* [@drawbotapp on Twitter](https://twitter.com/drawbotapp)
* [Drawbot Forum](https://forum.drawbot.com)
* [Drawbot Skia](https://github.com/justvanrossum/drawbot-skia) for cross-platform use (in-development)
* [Python for Designers](http://www.pythonfordesigners.com), a beautifully-designed Drawbot walkthrough by [Roberto Arista](http://projects.robertoarista.it)
* [RoboDocs Drawbot Examples](https://github.com/roboDocs/drawBotExamples)

### Python resources
* [Python Documentation](https://docs.python.org/3/)
* [Python Beginner’s Guide for Non-Programmers](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)

### Drawbot Modules
* [Pagebot](https://github.com/PageBot/PageBot)
* [Furniture](https://github.com/stenson/furniture) animation tools by Rob Stenson ([blog post](https://robstenson.com/articles/animating-with-drawbot.html))
* [DrawBotModules](https://github.com/danielgamage/DrawBotModules)
* [drawbotlab](https://github.com/djrrb/drawbotlab) (is this deprecated?)

### Drawbot projects
* [BadgeBot](https://github.com/djrrb/badgebot), my conference badges for the first [Typographics](https://2015.typographics.com) conference
* [Daily Drawbot](https://dailydrawbot.tumblr.com), fun animations by [Just van Rossum](https://twitter.com/justvanrossum)
* [Lowlands](http://hansje.net/Lowlands-2017) by [Hansje van Halem](http://hansje.net) and [Just van Rossum](https://twitter.com/justvanrossum)
* [Drawbot Plotter](https://github.com/jenskutilek/DrawBotPlotter) by Jens Kutilek
* [Incomplete Cubes Generator](https://github.com/robweychert/incomplete-cubes-generator) by Rob Weychert
* [Old Glory](https://github.com/djrrb/OldGlory) flag generator by me
* [Overlay PDF](https://github.com/scribbletone/overlay-pdf) by scribbletone
* [Reticulate](https://github.com/werls/reticulate) (halftone) by Werllen Castro
* [Maurice Meilleur](https://mauricemeilleur.net)
* [Recursive font](https://github.com/arrowtype/recursive/tree/e953d2a890bf3edce60daec4b467be79313a11a0/src/proofs/drawbot-specimens-and-diagrams) by Arrow Type

### Drawbot script collections

* [Agyei Archer](https://github.com/agyeiarcher/drawbot/)
* [Alphabet Type](https://github.com/AlphabetType/DrawBot-Scripts) (robofont only)
* [Eli Heuer](https://github.com/eliheuer/drawbot-exercises)
* [Felipe Negrão](https://github.com/filipenegrao/drawbotScripts)
* [Future Fonts](https://github.com/futurefonts/type-animations)
* [Guido Ferreyra](https://github.com/guidoferreyra/Drawbot)
* [Ike Stevens](https://github.com/ikestevens/Drawbot)
* [Jesen Tanadi](https://github.com/jtanadi/drawbotSketches)
* [Johannes Lang](https://github.com/jo-lang/drawbotscripts)
* [Josef Renner](https://github.com/oolong32/drawbot-exercises)
* [Maarten Renckens](https://github.com/Artengar/Drawbot)
* [Mark Frömberg](https://github.com/Mark2Mark/DrawBot-GitHub)
* [Matthew Smith](https://github.com/mttymtt/DrawBot-Sketchbook)
* [Max Kohler](https://github.com/awesomephant/drawbot-experiments)
* [medthehatta](https://github.com/medthehatta/drawbot)
* [Nina Stössinger](https://github.com/ninastoessinger/DrawBot-Scripts)
* [Rosetta Type](https://github.com/rosettatype/drawbot-scripts)
* [Ryan Bugden](https://github.com/ryanbugden/Drawbot)
* [Sebastian Carewe](https://github.com/eweracs/drawbot-scripts)
* [Shin Chu](https://github.com/shinchu/drawbot_sketches)
* [Stephen Nixon](https://github.com/thundernixon/drawbot)

