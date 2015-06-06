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
    elif binary1[0]=='0' and binary2[0]=='0':
        return '0'+addBinary(binary1[1:],binary2[1:])
    elif binary1[0]=='1' and binary2[0]=='0':
        return '1'+addBinary(binary1[1:],binary2[1:])
    elif binary1[0]=='0' and binary2[0]=='1':
        return '1'+addBinary(binary1[1:],binary2[1:])
    elif binary1[0]=='1' and binary2[0]=='1':
        return '0'+addBinary(addOne(binary1[1:]),binary2[1:])
    else:
        return

def testAddBinary():
    print(addBinary('01','11')=='101')
    print(addBinary('1','110')=='001')
    print(addBinary('','11')=='11')
    print(addBinary('11','')=='11')

def intToBinary(inte):
    c=inte
    b=''
    a=0
    while not(c//2==0 and c%2==0):
        a=c%2
        c=c//2
        b=b+str(a)
    return b

def testIntToBinary():
    print(intToBinary(2)=='01')
    print(intToBinary(6)=='011')
    print(intToBinary(0)=='')
    print(intToBinary(8)=='0001')

def binaryToInt1(bi):
    b=1
    c=0
    d=0
    for word in bi:
        a= int(bi[d])*b
        b=b*2
        c=c+a
        d+=1
    return c

def main():
    #testIsZeroBinaryString()
    #testAddOne()
    #testAddBit()
    #testAddBinary()
    testIntToBinary()
    #testBinaryToInt1()

main()
 
