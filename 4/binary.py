
def isZeroBinaryString(binaryString):
    if len(binaryString)==0:
        return True
    elif binaryString[0]=='1':
        return False
    else:
        return isZeroBinaryString(binaryString[1:] )

def testIsZeroBinaryString():
    print(isZeroBinaryString('0')==True)
    print(isZeroBinaryString('')==True)
    print(isZeroBinaryString('000')==True)
    print(isZeroBinaryString('010')==False)

def addOne(binary):
    if len(binary)==0:
        return '1'
    elif binary[0]=='0':
        return '1'+binary[1:]
    else:
        return '0'+addOne(binary[1:])

def testAddOne():
    print(addOne('00')=='10')
    print(addOne('')=='1')
    print(addOne('01')=='11')
    print(addOne('11')=='001')

def main():
    testIsZeroBinaryString()
    testAddOne()
    #testAddBit()
    #testAddBinary()
    #testIntToBinary()
    #testBinaryToInt1()

main()
 
