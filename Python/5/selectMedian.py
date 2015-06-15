
import time
def quickSelect(aList,k):
    if  len(aList)!=0:
        pivot =aList[len(aList)//2]
        smallerList = []
        largerList = []
        count = 0
        for  i in aList:
            if i<pivot:
                smallerList +=[i]
            elif i>pivot:
                largerList+= [i]
            else:
                count+= 1
        
        m =  len(smallerList)
        if k >= m and k < m+count:
            return pivot
        if m>k:
            return quickSelect(smallerList,k)
        else:
            return quickSelect(largerList,k-m-count)

def simplisticApproach(filename):
    location =[]
    for line in open(filename):
        line=line.split()
        location.append(int(line[1]))
            return location
                print (location)

def computeSum( aList, med ):
    sum=0
    for inte in aList:
        if inte>med:
            sum +=inte-med
        else:
            sum+=med-inte
    return sum

def Median(location):
    if len(location)%2==0:
        index =len(location)//2
        
        
        med1 = int(quickSelect(location,index))
        med2 = int(quickSelect(location,index-1))
        med = (med1 + med2)//2
        return med
    else:
        index=len(location)//2
        print("odd")
        return quickSelect(location,index)


def main():
    total =0
    start=0
    
    filename=input("Enter filename")
    start=time.clock()
    print(simplisticApproach(filename))
    location=   simplisticApproach(filename)
    #med=Median(location)
    
    #print("median =" ,med)
    print("sum of distance = ", computeSum( location, med ) )
    
    print(time.clock()-start)

main()




