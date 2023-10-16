import turtle
def Paint_Circle(t,x,y, radius, penSize, penColor, fillColor):
    t.penup()
    t.home()
    t.goto(x,y)
    t.pendown()
    t.pencolor(penColor)
    t.pensize(penSize)
    t.fillcolor(fillColor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
