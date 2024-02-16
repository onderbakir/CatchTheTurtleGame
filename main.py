from turtle import *
import time
import random

#background
background_board = Screen()
background_board.bgcolor("purple")
background_board.title("Catch the Turtle")

#property to use
style=("courier",28,"italic")
time_off=20
score=0

#Catch turtle
turtle_instance = Turtle()

#Catch turtle property
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.hideturtle()

#Count turtle
count_turtle = Turtle()

#Count turtle property
count_turtle.hideturtle()
count_turtle.penup()

#Score turtle
score_turtle = Turtle()

#Score turtle property
score_turtle.hideturtle()
score_turtle.penup()

#Turtle holding time sign
time_hold_turtle = Turtle()

#Time_hold_turtle property
time_hold_turtle.hideturtle()
time_hold_turtle.penup()
time_hold_turtle.goto(-100,260)
time_hold_turtle.write("Time: ",font=style)

#introductory text
introductory_turtle = Turtle()

#introductory_turtle property
introductory_turtle.hideturtle()
introductory_turtle.penup()

#Score turtle function
def click(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.color("black")
    score_turtle.goto(-100, 225)
    score_turtle.write("Score: {}".format(score), font=style)

while True:
    #count_turtle property

    count_turtle.color("white")
    count_turtle.goto(0,260)
    count_turtle.write(time_off,font=style, align="left")

    #introductory_turtle start loop
    if time_off == 20 :
        introductory_turtle.write("Go",font=style,align="center")

    time.sleep(1)
    time_off -= 1

    count_turtle.clear()

    #introductory_turtle finish loop
    if time_off == 19:
        introductory_turtle.clear()


    #catch turtle property
    turtle_instance.hideturtle()
    turtle_instance.penup()


    if time_off == 0:
        count_turtle.clear()
        count_turtle.write("--End--",font=style)
        break

    #Catch turtle random position and property
    if time_off % 1 == 0:
        turtle_instance.goto(10+random.randint(-250,220),10+random.randint(-250,220))
        turtle_instance.showturtle()

    #Detect click
    turtle_instance.onclick(click)

mainloop()