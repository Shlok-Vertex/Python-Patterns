from turtle import *
from colorsys import *

speed(0)
bgcolor("black")
h = 0
pensize(3)
def design(x,y):
    circle(y * 1.2,90)
    left(x)
    circle(y * 1.2,90)

for i in range(89):
    pencolor(hsv_to_rgb(h,1,1))
    design(135,i)    
    design(135,i)    
    design(90,i)    
    design(135,i)    
    design(135,i)
    h += 0.0020
    hideturtle()
done()

