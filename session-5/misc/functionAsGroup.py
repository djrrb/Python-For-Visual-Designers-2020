def myGroup(x, y):
    fill(1, 0, 0)
    rect(0, 0, 50, 50)
    fill(0, 1, 0)
    oval(50, 0, 50, 50)
for i in range(30):
    with savedState():
        translate(randint(0, width()), randint(0, height()))
        myGroup()