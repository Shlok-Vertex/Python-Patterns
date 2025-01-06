from turtle import *
from colorsys import *
tracer(20)
bgcolor("black")
h = 0.95
for i in range(400):
    pencolor(hsv_to_rgb(h,1,1))
    h += 0.0011
    right(119)
    circle(-i*0.3,120)
    circle(i*0.3,120)
    circle(-i*0.1,120)
done()  
    
    
