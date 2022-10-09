from turtle import *
from keyboard import *
input("Bienvenue dans le jeu du morpion crée par Frunix.\n Appuyer sur entrée pour commencer.")
J1=input("Pseudo du joueur 1: ")
J2=input("Pseudo du joueur 2: ")
speed(99)
hideturtle()
pu()
goto(0,0)
pd()
forward(99)
pu()
goto(0,33)
pd()
forward(99)
pu()
goto(33,-33)
right(-90)
pd()
forward(99)
pu()
goto(66,-33)
pd()
forward(99)
pu()
for i in range(9) :
    print("Au tour de", J1)
    # fonction pour placer 
    def placerJ1(nombre):
        color("red")
        if nombre=="1":
            pu()
            goto(16.5,-16.5)
            pd()
            circle(10)
        elif nombre=="2":
            pu()
            goto(60,-16.5)
            pd()
            circle(10)
        elif nombre=="3":
            pu()
            goto(99,-16.5)
            pd()
            circle(10)
        elif nombre=="4":
            pu()
            goto(16.5,16.5)
            pd()
            circle(10)
        elif nombre=="5":
            pu()
            goto(60,16.5)
            pd()
            circle(10)
        elif nombre=="6":
            pu()
            goto(99,16.5)
            pd()
            circle(10)
        elif nombre=="7":
            pu()
            goto(16.5,60)
            pd()
            circle(10)
        elif nombre=="8":
            pu()
            goto(60,60)
            pd()
            circle(10)
        elif nombre=="9":
            pu()
            goto(99,60)
            pd()
            circle(10)
                
    nombre=input("Où souahites-tu placer ton rond bleu?") 
    placerJ1(nombre)
    print("Au tour de", J2)
    # fonction pour placer 
    def placerJ2(nombre):
        color("blue")
        if nombre=="1":
            pu()
            goto(16.5,-16.5)
            pd()
            circle(10)
        elif nombre=="2":
            pu()
            goto(60,-16.5)
            pd()
            circle(10)
        elif nombre=="3":
            pu()
            goto(99,-16.5)
            pd()
            circle(10)
        elif nombre=="4":
            pu()
            goto(16.5,16.5)
            pd()
            circle(10)
        elif nombre=="5":
            pu()
            goto(60,16.5)
            pd()
            circle(10)
        elif nombre=="6":
            pu()
            goto(99,16.5)
            pd()
            circle(10)
        elif nombre=="7":
            pu()
            goto(16.5,60)
            pd()
            circle(10)
        elif nombre=="8":
            pu()
            goto(60,60)
            pd()
            circle(10)
        elif nombre=="9":
            pu()
            goto(99,60)
            pd()
            circle(10)


    nombre=input("Où souahites-tu placer ton rond rouge ?") 
    placerJ2(nombre)


input()
