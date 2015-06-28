
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




                
def main():
    print('Hello')
    
main()
