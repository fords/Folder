
def createBin(size):
    """create the bin with 0 numbers representing free spaces """
    bin1=[]
    for row in range(size):
        bin1.append([])
        for col in range(size):
            bin1[row].append(0)
    return bin1

def check(bin1):
    """check the bin if it is free or not  """
    for row in range(len(bin1)):
        for col in range(len(bin1)):
                print(bin1[row][col], end=' ')
        print()
    print()

def readPut(size,name):
    """read the sizes of the blocks the filename given by user and make a list """
    blosize=[]
    filename=name
    a=open(name).read().strip()
    
    for char in a.split(' '):
        
        blosize.append(int(char))
    
    blosize=sorted(blosize,reverse=True)
    
    return blosize

def descPutFit(size,bin1,block,row,col):
    """check the blocks can be fitted into bin """
    if row+block>size:
        return False
    elif col+block>size:
        return False
    else:
        for x in range(row,row+block):
            for y in range(col,col+block):
                if bin1[x][y]!=0:
                    return False
        return True

def findOpenSpot(size,bin1,i,unpacked):
    """put the blocks in the available spaces and can show the final state of bin
        freespace and unpacked """
    Freespace=0
    for r in range(len(bin1)):
        for c in range(len(bin1)):
            if descPutFit(size,bin1,int(i),r,c)==True:
                bin1,Freespace=putBin(size,bin1,i,r,c)
                check(bin1)
                return bin1,Freespace,unpacked


unpacked.append(i)
return bin1,Freespace,unpacked



def putBin(size,bin1,block,row,col):
    """put the blocks into the bin and count the free space  """
    for r in range(row, row+block):
        for c in range(col,col+block):
            bin1[r][c]=block
    
    count=0
    for r in range(len(bin1)):
        for c in range(len(bin1)):
            if bin1[r][c]==0:
                count+= 1
    return bin1 ,count


                
def main():
    size=int(input("Enter the size of bins"))
    file=input("Enter the filename")
    bin1=createBin(size)
    block=readPut(size,file)
    
main()
