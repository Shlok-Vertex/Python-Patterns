from turtle import *
from colorsys import *
setposition(-40,35)
tracer(20)
bgcolor("black")
h = 0.60
pensize(1.5)
for i in range(150):
    h -= 0.0015
    color(hsv_to_rgb(h,1,1))
    fd(40)
    circle(160-i,100)
    left(90)
    circle(160-i,100)
    right(80)
    hideturtle()
    
done()    