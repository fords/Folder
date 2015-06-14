I built the function by using recursive for isZeroBinaryString(),addOne() and addBinary()
, iteration for binaryToInt() and intToBinary(), and addBit() uses addOne() for implementation.

testIsZeroBinaryString() tests '0','','010' and '000' for it is 0 or not;and the test case is important to know whether it returns true for 
0 and '',and fasle for 1

testAddOne() tests '00','','01' and '11' for adding 1 to binary number 
I input nothing '' for output 1 and input 00,01 and 11 strings to know that addOne() function is working correctly

testAddBit() tests bit=1 or 0 ;and if bit is 1,1 should be added to binary ,else bit is 0 ,nothing is added to binary.
I input bit 1 with binary '101' and '010',the output should be added by 1
input bit is 0 with 010 ,the output is 010 the same as input binary number
input bit is none of 1 or 0 ,the output is ''
The testAddbit() makes sure that the fuction is working right for adding 1 to binary number or not when bit is 1 or 0

testAddBinary() tests 01 and 11 the output is 101
1 and 110 ,output is 001
'' and '11' ,output is 11
11 and '' ,output is 11
test is important for if one string is nothing and another is a number,the output should be the number, and
to add both binary numbers to the correct way 

testBinaryToInt() tests '','01','10' and '111' for changing binary to integer
test is important for if input is nothing ,the output should be zero and to know the function is working

testIntToBinary() tests 2,6,0 and 8 for output which is binary number
test is important for if input is zero, out should be nothing and to know the function is working in the way as it should be.