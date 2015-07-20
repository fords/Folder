import random
class CircularLinkedList():
    """ contatinre for CircularLinkedlins"""
    __slots__ = ("head", "tail", "size",)
class EmptyNode():
    """An empty list is represented by an instance of Empty"""
    __slots__ = ()
class Node():
    """container for node"""
    __slots__=('data','next')
def mkNode(data, next):
    """mkNode: AnyType, LinkedList -> Node"""
    node = Node()
    node.data = data
    node.next = next
    return node
def mkCList():
    """ mKCList: None->Linkedlist"""
    lst = CircularLinkedList()
    lst.head = mkEmptyNode()
    lst.tail = mkEmptyNode()
    lst.size = 0
    return lst

def mkEmptyNode():
    """mkEmpty: None -> EmptyNode"""
    return EmptyNode()

def printList(lst):
    """prints the linked list """
    #if lst.size ==0:
     #   print("No node")

    print(lst.head.data, end= ' ' )
    temp=lst.head.next
    while temp!=lst.head:
        print(temp.data, end=' ')
        temp=temp.next
    print()

def remove(lst):
    """ remove function removes the elements till the one left and
   it removes the element at the head
   remove :lst ->anytype|None"""
    if lst.size==0:
       return EmptyNode
    elif lst.size==1:
        temp=lst.head
        lst.head=EmptyNode
        lst.tail=EmptyNode
        lst.size=lst.size-1
        return temp
    else:                      
        temp=lst.head
        lst.tail.next=lst.head.next
        lst.head=lst.head.next
        lst.size=lst.size-1
        return temp

                         
def add(lst,element):
    """add the element to the list at the tail
    add: lst*anytype ->None"""
    
    if isinstance(lst.head,EmptyNode):
        a =mkNode(element, lst.tail)
        lst.head=a
        lst.tail=a
        lst.size+=1
    else:
        
        a=mkNode(element,lst.head)
        lst.tail.next=a        
        lst.tail=a
        lst.size+= 1

       

   

def advance(lst):
    """ moves the head and the tail to the next linkedlist
    advance: lst ->anytype"""
   
    temphead=lst.head
   
    lst.tail= lst.head
    lst.head = lst.head.next
    return temphead

"""def remove(lst):
    if nextCursor(lst)==lst.head:
        a=lst.head
        a=a.next
        lst.head=a
    else:
        cur.next=cur.next.next
        size=size-1"""
def get1(lst):
    """ get the next element in the list
      get: lst -> anytype"""
    node=lst.head
    node=node.next
    return node.data

def size(lst):
    """ get the size of linkedlist
      size : list -> integer"""
    return lst.size

def player(filename):
    """play the game by removing one player per game and choose IT who choose
goose and try to get the place of goose
    player: str->None"""
    lst=mkCList()
    count=1
    lst.size=0
    for line in open(filename):
        line=line.strip()
        add(lst,line)
  
        
    print("size after the adding"+str(size(lst)))
    while not (size(lst)==1):
        #goose=lst.tail.data
        
        IT=lst.head.data
       # tempIT=lst.head
        #b=get1(lst)
        print(IT+" becomes IT")
        
        remove(lst)
        
        
        
        while random.random()<.75:
            duck=lst.head.data
            print(duck+'becomes duck')
            advance(lst)
            
        goose=lst.head.data
        print(goose+' becomes goose!')
        
        
        if random.random()<0.5:
            #goose wins,goose stays in the same place
            # IT doesn't have to be same person.change IT
            #remove(lst)
            print('goose '+goose+' wins')
            advance(lst)
          
            
                      
        else:
            
            remove(lst)
            add(lst,IT)
            
            #lst.head.data=IT
            print('IT ' ,IT,' wins')
            while (lst.size>0):
                if (lst.head.data==IT):
                    advance(lst)
                    break
                else:
                    advance(lst)
          
                    
           
        
        print("END round ",count)
        count+=1    
    print(size(lst))

def testList():
    """ testList: None->None"""
    print("new empty list")
    lst=mkCList()
    print("the size of the list is " + str(size(lst)))
    add(lst,10)
    add(lst,15)
    add(lst,20)
    printList(lst)
    print(lst.size,'before')
    remove(lst)
    remove(lst)
 
    printList(lst)
    print(lst.size)
    print(20==get1(lst))
    add(lst,1)
    add(lst,3)
    add(lst,5)
    printList(lst)
    print( lst.head==advance(lst))
    print(lst.head.data==1)
