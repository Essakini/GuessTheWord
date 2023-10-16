import gui
import drwacircle
import AmbAttemp
import PaintT
import time
import turtle

def Paint_Rectangle(t,x, y, dimX, dimY, penSize, penColor, fillColor):
    t.penup()
    t.home()
    t.goto(x,y)
    t.pendown()
    t.pencolor(penColor)
    t.pensize(penSize)
    t.fillcolor(fillColor)
    t.begin_fill()
    t.right(180)
    for i in range(2):
        t.forward(dimX)
        t.left(90)
        t.forward(dimY)
        t.left(90)
    t.end_fill()
