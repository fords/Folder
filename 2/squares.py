
from turtle import *

	
  
def drawSquare2(length,d):
    if d<0:
            return
    if d%2==0:
        color('red')
    else:
        color('green')
    up()
    forward(length/2)
    left(90)
    down()
    forward(length/2)
    right(180)
    drawSquare2(length/2, d-1)
    if d%2==0:
        color('red')
    else:
        color('green')
    right(90)
    forward(length)
    left(180)
    drawSquare2(length/2, d-1)
    if d%2==0:
        color('red')
    else:
        color('green')
    right(90)
    fd(length)
    left(180)
    drawSquare2(length/2, d-1)
    if d%2==0:
        color('red')
    else:
        color('green')
    right(90)
    fd(length/2)
    left(90)
    fd(length/2)
    right(90)
	   
def oneSquare(length,d):
    if d<0:
        return
    if d%2==0:
        color('red')
    else:
        color('green')
    up()
    fd(length/2)
    left(90)
    down()
    fd(length/2)
    left (180)
    drawSquare2(length/2,d-1)
    if d%2==0:
        color('red')
    else:
        color('green')
    right(90)	 
    fd(length)
    left(180)
    drawSquare2(length/2, d-1)
    if d%2==0:
        color('red')
    else:
        color('green')
    right(90)
    fd(length)
    left(180)
    drawSquare2(length/2,d-1)
    if d%2==0:
        color('red')
    else:
        color('green')
    right(90)
    fd(length)
    left(180)
    drawSquare2(length/2,d-1)
    if d%2==0:
        color('red')
    else:
        color('green')
    right(90)
    fd(length/2)
    	
	#inner square complete


def main():
	setup(600,600)
	pensize(2)
	speed(0)
	
	setworldcoordinates(-202,-202,202,202)
	hideturtle()
	d=int(input("Enter depth"))
	oneSquare(200,d)
	input('press enter')
	showturtle()
	bye()
  
  


# runs program from here




main()
 
	
	
