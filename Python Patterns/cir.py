from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h = 0
for i in range(220):
    h += 0.0015
    color(hsv_to_rgb(h,1,1))
    goto(0,0)
    circle(70,50)
    rt(30)
    fd(i)
    rt(90)
    for j in range(3):
        rt(70)
        fd(70)
        rt(80)
    hideturtle()
done()        