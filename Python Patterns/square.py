from turtle import *
setposition(-60,0)
speed(0)
bgcolor("black")
colors = ["orange","white"]
pensize(2)
for i in range(150):
    color(colors[i % 2])
    rt(i)
    circle(90,i)
    up()
    fd(i+50)
    down()
    rt(90)
    fd(i-65)
    hideturtle()
done()    