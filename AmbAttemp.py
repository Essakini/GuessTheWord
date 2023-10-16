import gui
import drwacircle
import Drawsquare
import AmbAttemp
import PaintT
import time

#switch that drwas the ambulance when called in game along with faild variable 
import turtle

def Ambulance(attempt):
    if (attempt == 1):
        Drawsquare.Paint_Rectangle(gui.tMain,gui.offset_x,gui.offset_y,200,150,4,"blue","lavender")
    elif(attempt ==2):
        Drawsquare.Paint_Rectangle(gui.tMain,110 + gui.offset_x,-40 + gui.offset_y,110,110,4,"blue","lavender")
    elif(attempt ==3):
        drwacircle.Paint_Circle(gui.tMain,-130 + gui.offset_x,-190 + gui.offset_y,40,4,"blue","blue")
    elif(attempt == 4):
        drwacircle.Paint_Circle(gui.tMain,30 + gui.offset_x,-190 + gui.offset_y,40,4,"blue","blue")
    elif(attempt == 5):
        Drawsquare.Paint_Rectangle(gui.tMain,90 + gui.offset_x,-50 + gui.offset_y,70,30,4,"blue","lavender")
    elif(attempt == 6):
        Drawsquare.Paint_Rectangle(gui.tMain, -80 + gui.offset_x, 20 + gui.offset_y, 35,20,4,"blue","red")
    elif(attempt == 7):
        Drawsquare.Paint_Rectangle(gui.tMain,-60 + gui.offset_x,-40 + gui.offset_y,70,30,4,"red","red")
    elif(attempt ==8):
        Drawsquare.Paint_Rectangle(gui.tMain,-80 + gui.offset_x,-20 + gui.offset_y,30,70,4,"red","red")

            #turtle.sleep(3)
    #turtle.exitonclick()
