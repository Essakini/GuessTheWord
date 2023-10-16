import gui #calling the turtles by area
import drwacircle # has the draw circle function
import Drawsquare # has the draw square function
import AmbAttemp # switch function that draws the the Ambulance depedning fon fail
import PaintT #calling the write on turtles function
import ImageT # contaning the layout of the game
import turtle
import string
import time
import math


#starting the game#
def Wgame():
        again = True
        count_p1=0
        count_p2=0
        condition_of_player=0 #variable that define whos player turn

        #getting players name with not control condition (it could be easly implemented controls for variable word and guess if required )
        player1=turtle.textinput("P1 Name","Player 1 insert your name:")
        player1=player1.capitalize()
        player2=turtle.textinput("P2 Name","Player 2 insert your name:")
        player2=player2.capitalize()

        while(again): # when user press esc or cancel game ends
            fail = 0
            simbolIN=True
            errors = "" #used to record user input errors
            #check which player should play seking if condition is odd or even
            if ((condition_of_player % 2) == 0 ):
                p1=player1
                p2=player2
            else:
                p1=player2
                p2=player1
            #starting the turtle in game text funtion to output the turtle
            ImageT.ingametext("You have 8 attempt left","","")
            #Import the word from Player1
            word = turtle.textinput(p1, "Enter your word (Make sure "+p2+" is no peaking!): ")
#word can contain space but not limit char has been implemented
            #getting word input and perform control techniques
            if (word is None):#if user press esc output is none and game ends
                esc="esc"
                gui.tMain.clear()
                ImageT.goodbytext(player1,player2,count_p1,count_p2)
                turtle.exitonclick()
                again=False
            while ( len(word)==0 or word.startswith(' ') ):#checking the sta
                if len(word) == 0:
                    word = turtle.textinput("Error","No value entred")
                elif(word.startswith(' ')):
                     word = turtle.textinput("Error","The 1st letter cannot start with space")
            while(simbolIN is True):
                for i in range (len(word)):
                    if(word[i] is not " " ):
                        if( ord(word[i])>122 or ord(word[i]) < 65  or (ord(word[i])>91 and ord(word[i])<96)  ):break
                else: simbolIN=False
                if(simbolIN is True):
                     word = turtle.textinput("Error","#Must enter only Letters#")
                     while(word.startswith(' ') or len(word)==0 ):
                         if(len(word)== 0):
                             word = turtle.textinput("Error","Must enter at least a letter")
                         elif(word.startswith(' ')):
                              word = turtle.textinput("Error","The 1st letter cannot start with space")


            #getting descriptionword input and perform control techniques
            descriptionword= turtle.textinput(p1, "Insert description to help "+p2+" at the 5th attempt ")
            if descriptionword==None:
                descriptionword="No help but you can do it!"
            else:
                while (len(descriptionword)==0 or len(descriptionword)>16 or descriptionword.startswith(' ')):
                    descriptionword= turtle.textinput(p1, "Max 16 char - do not start with space or empty input, try again")

            stars = list ("*" * len (word))
            stars_str = "" #variable to print stars on turtle
            for i in range (len(stars)):
                if word[i]==" ":
                    stars[i]="-"
                stars_str = stars_str + stars[i]+"   "
            word=word.lower() #change the any char in lower case as checks already perfomed
            ImageT.star(stars_str)#calling fuction in ImageT

            #if attempt less than 8 and stars is not as words then enter the loop
            while( fail < 8 and stars != list(word)):
                #seeting turtle to normal layout and design
                turtle.bgcolor("yellow")
                PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,-gui.leftUP_Y+100, "Wrong guesses: ","Green",("Times New Roman", 30 ,"italic"))
                PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Blue",("Times New Roman", 30 ,"italic","bold"))
                gui.tStars.clear()
                PaintT.Paint_Text(gui.tStars,gui.leftUP_X+10,gui.leftUP_Y-100, stars_str,"Blue",("Times New Roman", 30 ,"italic","bold"))
                time.sleep(.5)
                #if at the 5th attempt provide help inserted by p1 if not add string
                if(fail>=5):

                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-50, "To help you "+p1+" said:","Black",("Times New Roman", 30 ,"italic","bold"))
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-150, descriptionword,"Black",("Times New Roman", 30 ,"italic","bold"))

                #getting guess input and perform control techniques
                guess = turtle.textinput(p2,"Guess a letter: ")
                if (guess is None):
                    fail=8
                    esc="esc"
                    gui.tMain.clear()
                    ImageT.goodbytext(player1,player2,count_p1,count_p2)
                    turtle.exitonclick()
                    again=False
                    break
                guess=guess.lower()
                #perform 1st  input control
                while(len(guess)>1 or guess==" " or len(guess)==0 ):
                    if( len(guess)>1 ):
                        guess = turtle.textinput("Error","You must only enter one letter at the time")
                    elif(len(guess)== 0):
                        guess = turtle.textinput("Error","No value given")
                    elif(guess.startswith(' ')):
                         guess = turtle.textinput("Error","The 1st letter cannot start with space")
                #perform 2nd  input control
                while(guess not in string.ascii_lowercase):
                    guess = turtle.textinput("Error","#Must enter only Letters#")
                    while( len(guess)>1 ):
                            guess = turtle.textinput("Error","You must only enter one letter at the time")
                    while(len(guess)== 0):
                            guess = turtle.textinput("Error","No value given")
                    while(guess.startswith(' ')):
                             guess = turtle.textinput("Error","The 1st letter cannot start with space")

                #3rd check: if the guess is part of error list
                cf=True #flag variable
                if( errors.count(guess)>0):
                    while (cf is True ):
                        for i in range(len(errors)):
                            if(errors[i] == guess):break
                        else:cf=False#if guess not part of error than flag down out of loop

                        if(cf is True): #if flag still up then imput check again
                            guess= turtle.textinput("Error","Incorrect letter already inserted")
                            while(len(guess)>1 or guess==" " or len(guess)==0 ):
                                if(len(guess)>1):
                                    guess = turtle.textinput("Error","You can only enter one letter at the time")
                                else:guess = turtle.textinput("Error","No Value inserted")
                            while(guess not in string.ascii_lowercase):
                                if (len(guess)>1):
                                    guess = turtle.textinput("Error","You can only enter one letter at the time")
                                elif(len(guess)== 0 or guess==" "):
                                    guess = turtle.textinput("Error","No value given")
                                else:guess = turtle.textinput("Error","Must enter only a letter")

                #checking if guess is word
                if( word.count(guess)>0):
                    for i in range(len (word)):
                        #if guess is in word then screen change
                        if word[i].lower() == guess.lower():
                            turtle.bgcolor("green")
                            PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Yellow",("Times New Roman", 30 ,"italic","bold"))
                            stars [i] = guess
                            PaintT.Paint_Text(gui.tStars,gui.leftUP_X+10,gui.leftUP_Y-100, stars_str,"Yellow",("Times New Roman", 30 ,"italic","bold"))
                else:
                    #if guess is not paart then error screen and draw the turtle
                    errors = errors + guess
                    fail = fail + 1
                    turtle.bgcolor("red")
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,-gui.leftUP_Y+100, "Wrong guesses: ","Yellow",("Times New Roman", 30 ,"italic"))
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Yellow",("Times New Roman", 30 ,"italic","bold"))
                    PaintT.Paint_Text(gui.tStars,gui.leftUP_X+10,gui.leftUP_Y-100, stars_str,"Yellow",("Times New Roman", 30 ,"italic","bold"))
                    AmbAttemp.Ambulance(fail)
                stars_str = ""
                for i in range(len(stars)):
                    stars_str = stars_str + stars[i]+"   "
                errors_str = "       "
                for i in range(len(errors)):
                    errors_str = errors_str + errors[i]+"  "
                for i in range (len(stars)):
                    if word[i]==" ":
                        stars[i]=" "
                ImageT.ingametext("You have "+str(8 - fail)+" attempt left",stars_str,errors_str)

            turtle.bgcolor("yellow")
            PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Blue",("Times New Roman", 30 ,"italic","bold"))
            gui.tStars.clear()
            PaintT.Paint_Text(gui.tStars,gui.leftUP_X+10,gui.leftUP_Y-100, stars_str,"Blue",("Times New Roman", 30 ,"italic","bold"))
            if(fail == 8):
                    #game lost by player and print screen
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-50, "YOU LOSE! ","Black",("Times New Roman", 30 ,"italic","bold"))
                    gui.tStars.clear()
                    PaintT.Paint_Text(gui.tStars,gui.leftUP_X+10,gui.leftUP_Y-100, "The word was:"+word,"Blue",("Times New Roman", 30 ,"italic","bold"))
                    time.sleep(0.2)
                    #condition below allow the swap of users
                    if((condition_of_player % 2) == 0 ):
                        count_p1=count_p1+1
                        condition_of_player=1
                    else:
                        count_p2=count_p2+1
                        condition_of_player=0 #condition flag when the loop restars
                    gui.tMain.clear()
                    gui.tAttempt.clear()
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Blue",("Times New Roman", 30 ,"italic","bold"))
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-150, p1+" score "+str(count_p1),"Black",("Times New Roman", 30 ,"italic","bold"))
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-100, p2+" score "+str(count_p2),"Black",("Times New Roman", 30 ,"italic","bold"))
            else:
                #game won by player and print screen
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-50, "YOU WIN!","Black",("Times New Roman", 30 ,"italic","bold"))
                    time.sleep(.5)
                    #condition below allow the swap of users
                    if((condition_of_player % 2) == 0 ):
                        count_p2=count_p2+1
                        condition_of_player=1#condition flag when the loop restars
                    else:
                        count_p1=count_p1+1
                        condition_of_player=0#condition flag when the loop restars

                    gui.tAttempt.clear()
                    gui.tMain.clear()
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Blue",("Times New Roman", 30 ,"italic","bold"))
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-150, p1+" score "+str(count_p1),"Black",("Times New Roman", 30 ,"italic","bold"))
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+450,gui.leftUP_Y-100, p2+" score "+str(count_p2),"Black",("Times New Roman", 30 ,"italic","bold"))
            esc=turtle.textinput("Play again?","Press any key to restart the game OR ESC TO END.")
            if (esc == "esc"):
                    #clear the turtle and send to good by function page
                    gui.tWrong.clear()
                    gui.tAttempt.clear()
                    gui.tStars.clear()
                    gui.tMain.clear()
                    ImageT.goodbytext(player1,player2,count_p1,count_p2)
                    turtle.exitonclick()
                    again=False

            else:
                    #clear the turtle before new game
                    gui.tWrong.clear()
                    gui.tAttempt.clear()
                    gui.tStars.clear()
                    gui.tMain.reset()
                    PaintT.Paint_Text(gui.tMain,gui.leftUP_X+10,gui.leftUP_Y-50, "Guess the word: ","Blue",("Times New Roman", 30 ,"italic","bold"))
                    #turtle.exitonclick()
                    again=True
                    #condition_of_player=condition_of_player+1


def main():
    gui.userI()#calling turtles from gui file
    Wgame()#game function 

main()
