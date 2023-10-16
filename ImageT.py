import gui
import drwacircle
import Drawsquare
import AmbAttemp
import PaintT
import time
import turtle

#function tha prints on screen the turtles with the arguments from the game file 
def ingametext(attempts,stars,errors):
    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Blue",("Times New Roman", 30 ,"italic","bold"))
    gui.tStars.clear()
    PaintT.Paint_Text(gui.tStars,gui.leftUP_X+10,gui.leftUP_Y-100, stars,"Blue",("Times New Roman", 30 ,"italic","bold"))
    gui.tAttempt.clear()
    PaintT.Paint_Text(gui.tAttempt,gui.leftUP_X+300,-gui.leftUP_Y+10,attempts,"Black",("Times New Roman", 20 ,"italic"))
    if(len(errors) > 0):
        PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,-gui.leftUP_Y+100, "Wrong guesses: ","Green",("Times New Roman", 30 ,"italic"))
        gui.tWrong.clear()
        PaintT.Paint_Text(gui.tWrong,gui.leftUP_X+10,-gui.leftUP_Y+50, errors,"Green",("Times New Roman", 30 ,"italic"))

#goodby function when the user clicks type esc or press esc
def goodbytext(player1,player2,count_p1,count_p2):
    #turtle.write('Home = ', align="center")

    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "SEE YOU NEXT TIME","Blue",("Times New Roman", 30 ,"italic","bold"))
    gui.tStars.clear()
    gui.tWrong.clear()
    gui.tAttempt.clear()
    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-100, "The Final Score: ","Blue",("Times New Roman", 30 ,"italic","bold"))
    if(count_p1>count_p2):
        PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-150,"1st place: "+ player1+" score "+str(count_p1),"Black",("Times New Roman", 30 ,"italic","bold"))
        PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-200, "2nd place:"+player2+" score "+str(count_p2),"Black",("Times New Roman", 30 ,"italic","bold"))
    elif(count_p1<count_p2):
        PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-150,"1st place: "+ player2+" score:"+str(count_p2),"Black",("Times New Roman", 30 ,"italic","bold"))
        PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-200, "2nd place:"+player1+" score:"+str(count_p1),"Black",("Times New Roman", 30 ,"italic","bold"))
    else:PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-350,player1+" score: "+str(count_p1)+"\n"+player2+" score: "+str(count_p2)+"\n IT'S A DRAW","Blue",("Times New Roman", 30 ,"italic","bold"))

#simple function to print the 1st output stars
def star(stars):
    gui.tStars.clear()
    PaintT.Paint_Text(gui.tStars,gui.leftUP_X+10,gui.leftUP_Y-100, stars,"Blue",("Times New Roman", 30 ,"italic","bold"))
