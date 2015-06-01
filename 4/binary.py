
def isZeroBinaryString(binaryString):
    
    if len(binaryString)==0:
        return True
    elif binaryString[0]=='1':
        return False
    else:
        return isZeroBinaryString(binaryString[1:] )

def main():
    testIsZeroBinaryString()
    testAddOne()
    testAddBit()
    testAddBinary()
    testIntToBinary()
    testBinaryToInt1()

main()
 
