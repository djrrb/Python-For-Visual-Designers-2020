import math
offset = -width()//2
step = 5
for x in range(offset, width()+offset+step, step):
    y = .004*x**2+0
    stroke(1, 0, .5)
    fill(None)
    rect(0, 0, x-offset, y)