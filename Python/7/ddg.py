"""use Linkedlist to find the player who wins in duck duck goose elimination
author :Zeyar Win
file ddg.py"""
from myList1 import *
import random
    
def main():
    """ ask the users the filename and random number and play the game"""
    seed=int(input("enter seed for the random number generator:"))
    random.seed(seed)
    filename=input("Enter the filename")
   
    player(filename)
    testList()
       
            
main()       
               
                 
      
                     
