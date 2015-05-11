"""
   Drawing many 3 quarter squares
   file Squrares_simpley.py
   author : Zeyar Win
"""
from turtle import *

d=int(input("Enter depth"))

def initialization():
    """
     
     set the window canvas size

    """
    setup(600,600)
    pensize(2)
    speed(0)
    
    setworldcoordinates(-202,-202,202,202)
  
def drawSquare2(length,d, c):
    if d<=0:
        pass
    
    else:
        
        if c == 'red' :
            c = 'green'
                color('green')
                    elif c == 'green' :
                        c = 'red'
    color('red')
    up()
    forward(length/2)
    left(90)
    down()
    forward(length/2)
    right(180)
    drawSquare2(length/2, d-1, c)
    right(90)
    forward(length)
    left(180)
    drawSquare2(length/2, d-1, c)
    right(90)
    fd(length)
    left(180)
    drawSquare2(length/2, d-1, c)
    right(90)
    fd(length/2)
    up()
    left(90)
    fd(length/2)
    right(90)
    down()
    if c == 'red' :
        c = 'green'
            color('green')
                elif c == 'green' :
                    c = 'red'
                        color('red')



  

      
    

def main():
    """
    
    wait for the user to press enter to end the program

    """
    initialization()
    drawSquare2(200,d, 'green')


# runs program from here
# main program
main()
 
    
    
