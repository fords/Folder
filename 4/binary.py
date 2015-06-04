"""
    Using recursion to do binary number adding each other and add one to
    binary number.There are iterations to invert binary to integer and vice versa
    filename binary.py
    
"""

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


def addBit(bit,binary):
    if bit=='0':
        return binary
    elif bit=='1':
        return addOne(binary)
    else:
        return ''

def testAddBit():
    print(addBit('1','101')=='011')
    print(addBit('','11')=='')
    print(addBit('1','010')=='110')
    print(addBit('0','010')=='010')

def addBinary(binary1,binary2):
    if len(binary1)==0 and len(binary2)==0:
        return ''
    elif len(binary1)==0 and len(binary2)!=0:
        return binary2[0:]
    elif len(binary1)!=0  and len(binary2)==0:
        return binary1[0:]

def main():
    #testIsZeroBinaryString()
    #testAddOne()
    testAddBit()
    #testAddBinary()
    #testIntToBinary()
    #testBinaryToInt1()

main()
 
