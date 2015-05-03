""" writing 'RIT TIGERS'
    file Name : RIT_tigers.py
    author Zeyar Win
"""
from turtle import *

def drawR():
    """ draws R """
    down()
    left(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(10)
    right(90)
    forward(30)
    left(135)
    forward(28)
    up()
    seth(0)
    forward(20)
    down()
    
def drawI():
    """ draws I """
    forward(30)
    left(180)
    forward(15)
    right(90)
    forward(30)
    left(90)
    forward(15)
    left(180)
    forward(30)
    right(90)
    up()
    forward(30)
    left(90)
    forward(10)
    down()
   
def drawT():
    """
      draws T 
    """
    
    up()
    forward(15)
    down()
    left(90)
    forward(30)
    left(90)
    forward(15)
    left(180)
    forward(30)
    up()
    forward(10)
    right(90)
    forward(30)
    left(90)
    down()

def drawG():
    """
      draw G
    """
    forward(30)
    left(90)
    forward(10)
    left(90)
    forward(10)
    up()
    forward(20)
    left(90)
    forward(10)
    left(180)
    down()
    forward(30)
    right(90)
    forward(30)
    up()
    right(90)
    forward(30)
    left(90)
    forward(10)
    down()


def drawE():
    """
        draw E
    """
    forward(30)
    left(180)
    forward(30)
    right(90)
    forward(15)
    right(90)
    forward(20)
    right(180)
    forward(20)
    right(90)
    forward(15)
    right(90)
    forward(30)
    up()
    right(90)
    forward(30)
    left(90)
    forward(10)
    down()

def drawS():
    """  draw S"""
    forward(30)
    left(90)
    forward(15)
    left(90)
    forward(30)
    right(90)
    forward(15)
    right(90)
    forward(30)
    up()
    right(90)
    forward(30)
    left(90)
    forward(10)
    down()
    

def main():
    """
      Draws 'RIT TIGER' by combining all of the functions 
    """
    drawR()
    drawI()
    drawT()
    up()
    forward(10)
    down()
    drawT()
    drawI()
    down()
    drawG()
    drawE()
    drawR()
    drawS()
  


    
    

speed(0)
  #run programs here
main()
input("Enter the key to end program")
