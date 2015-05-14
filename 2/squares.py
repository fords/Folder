"""
   Drawing many  squares at the edge of squares
   file Squrares_simpley.py
   author : Zeyar Win
"""
from turtle import *

	
  
def drawSquare2(length,d):
    """
        Draws 3 quarter squares recursively
            pre-condition penup and facing east
            post-condition pen down and facing east

    """
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
    """
        draw a full square with many 3 quarter squares
        precondition : facing east and pen down
        post condition:facing north and pen down
    """
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
	"""
    wait for the user to press enter to end the program

	"""
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
 
	
	
