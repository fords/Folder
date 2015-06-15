"""use python to find the index of the number in the unsorted list
  filename selectMedian.py
  author Zeyar Win"""


import time

def  simplisticApproach(filename):
     location =[]
     for line in open(filename):
         line=line.split()
         location.append(int(line[1]))
     return location   
     print (location)
#print(simplisticApproach('office.txt'))

def median(location):
    totalNo=len(location)
    if totalNo%2==0:
         return (int(location[totalNo//2-1])+int(location[totalNo//2]))/2
    else:
         return int(location[totalNo//2])

def computeSum( aList, med ):
    sum=0
    for inte in aList:
        if inte>med:
            sum +=inte-med
        else:
            sum+=med-inte
    return sum


def insertionSort(words):
    """insertionSort: list of words.
    Sorts a list of words in place."""

    # start marker at 1
    for marker in range(1,len(words)):
        # copy out the value at the marker
        marker_value = words[marker]
        i = marker
        
        # find place in list to store marker, shifting
        # predecessor values that are greater than up
        while i > 0 and words[i-1] > marker_value:
            words[i] = words[i-1]
            i -= 1
        # we have a home for the marker, store it
        words[i] = marker_value
    return words

  

def main():
    filename=input("Enter filename")
    start=time.clock()
    print(simplisticApproach(filename))
    location=   simplisticApproach(filename)
    
    sort=insertionSort(location)

    med=median(sort)
    print("median is " ,med)
  
    print("the sum of distance is ",computeSum(location,med))
    print(time.clock()-start)

main()

#42.918974692301255
