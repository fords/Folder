""" draw star

    file : star.py
    author : zeyar Win
    """
from turtle import *
def triangle():
    """
    draw  one triangle 
    """
    left(60)
    forward(20)
    right(120)
    forward(20)
    right(120)
    forward(20)
    
def manyTriangle():
    """
    draw totlal 5 triangles
    """
    seth(0)
    forward(20)
    right(72)
    triangle()
    left(180)
    forward(20)
    right(72)
    triangle()
    left(180)
    forward(20)
    right(72)
    triangle()
    left(180)
    forward(20)
    right(72)
    triangle()
    
    
    

def main():
    """
     The program waits for the user to respond to end the program"""
    triangle()
    manyTriangle()
   
    input ("Hit enter to end program")
    
    
    # begins run program here
    
speed(0)
main()
    
