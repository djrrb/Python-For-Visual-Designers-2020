with savedState():

    translate(width()/2)
    stroke(0, 0, 1)
    strokeWidth(4)

    with savedState():
        for i in range(10):
            translate(50, 50)
            scale(2)
            rotate(30)
            stroke(1, 0, 0)
            strokeWidth(4)
            oval(-5, -5, 10, 10)
       
    fill(0, 1, 0)
    rect(-20, -20, 40, 40)       
        
fill(1, 0, 0)
rect(-20, -20, 40, 40)