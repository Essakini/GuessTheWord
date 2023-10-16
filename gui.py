import turtle
#ini. the screen and turtles
def userI():
    turtle.setup (width=0.7 ,height=0.75, startx=300, starty=50)
    turtle.title("THE GAME")
    global tWrong
    tWrong = turtle.Turtle()
    tWrong.speed(0)
    global tAttempt
    tAttempt = turtle.Turtle()  #4 global variables contating the turtuels
    tAttempt.speed(10)
    global tStars
    tStars = turtle.Turtle()
    tStars.speed(0)
    global tMain
    tMain = turtle.Turtle()
    tMain.speed(10)



    tWrong.hideturtle()
    tAttempt.hideturtle()
    tStars.hideturtle()
    tMain.hideturtle()
    turtle.hideturtle()

    turtle.bgcolor("yellow")

#x,y coordinates
    global offset_x
    offset_x = 50
    global offset_y
    offset_y = 50

    global leftUP_X
    leftUP_X = -(turtle.window_width()/2)
    global leftUP_Y
    leftUP_Y = (turtle.window_height()/2)
