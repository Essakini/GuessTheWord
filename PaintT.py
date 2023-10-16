import turtle
#paint text on screen turtle when called along arguments
def Paint_Text(t,x,y,text,textcolor,textFont):
    t.penup()
    t.pencolor(textcolor)
    t.goto(x,y)
    t.write(text, True, font = textFont)
