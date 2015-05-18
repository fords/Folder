from turtle import *
speed(0)

def boxRec(length,side):
    if side<=0 or length<=0:
        pass
    else:
        fd(length)
        left(90)
        boxRec(length,side-1)
  
def drawFlowerRec(petal,length,d):
    if d<=0 or length<=0:
        pass
    else:
        if d%2==0:
            color('green')
        else:
            color('red')

        boxRec(length,4)
        left(360/petal)
        drawFlowerRec(petal,length,d-1)
    

def boxIt(length):
    side=4
    while side>0:
        fd(length)
        left(90)
        side =side-1

def drawFlowerIt(petal,length,d):
    d=petal
    while d>0 and length>0:
        if d%2==0:
            color('green')
        else:
            color('red')
        boxIt(length)
        left(360/petal)
        d  =d-1
        
   
def main():
    length =int(input("Enter the size"))
    petal=int(input("Enter the petal no."))
    setup(1000,1000)
    d=petal
    hideturtle()
    drawFlowerRec(petal,length,d)
    up()
    fd(340)
    down()
    drawFlowerIt(petal,length,d)
    showturtle()

main()
