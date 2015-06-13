


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


def main():

main()




