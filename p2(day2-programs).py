'''def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s=s+r**2
            n=n//10
        return s
n=int(input("enter the number:"))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("happy number")
else:
    print("not a happy number")'''

'''class encap:
    __a=10
    c=20
    def encapfunction(self):
        __b=200
        print("encap function-accessing protected")
        print(self.__a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
class encap:
    __a=10
    print(__a)
    def encapfunctin(self):
        print("encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)#will throw error because a is private,cannot be accessed
#outside class public'''

'''polymorphism:
one item or same item used for different purpose
types:
1-overloading:
    a-operator overloading
    b-method overloading
2-overriding'''

'''class m_overload:
    def display(self,a=None,b=None):
        print(a,b)
obj=m_overload()
print("without arguments")
obj.display()
print("with all arguments")
obj.display(20,30)
print("with one argument")
obj.display(10)'''

'''overriding:
if a method is defective or cannot be used inside a derived class it will take
it from its base class or parent class'''

'''class vijayawada():
    def placename(self):
        print("vijayawada placename is klu")
    def student(self):
        print("yes-vijayawada")
    def which_year(self):
        print("third year")
class hyd():
    def placename(self):
        print("hyderabad placename is hyd-klu")
    def student(self):
        print("yes-hyderabad")
    def which_year(self):
        print("third year-hyd")
obj_vij=vijayawada()
obj_hyd=hyd()
for detais in (obj_vij,obj_hyd):
    details.placename()
    detais.student()
    detais.which_year()'''

'''data structures using python:
1-helps to write efficient programs
2-linear:array,linked list,stack,queue,matrix
3-non linear:binary tree,heap,hash table,graph
4-linear:storing data sequently
5-non linear:no sequential style is required
6-array is an example of static linear data structure
7-list,stack and queue are example of dynamic linear data structures

linked list:
the real time example is train
as the name says list of items which are linked with one another is known as
linked list.
types:
1-single or singly
2-double or doubly
3-circular

creating linked list:
step1-create the node
step2-partition the node with two segments data and none
step3-add value into the blank node
step4-mark the node as head
step5-create the next node by following the above steps
step6-establish link between first node and the second node

displaying linked list:
traversal is required from first node till tail node in order to display
existing linked list.'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
obj.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
n.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist():
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_beginning(100)
obj.display()
print("")
print("after inserting 555")
obj.insert_beginning(555)
obj.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist():
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_end(111)
obj.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist():
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_position(2,100)
obj.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
a_llist=LinkedList()
n=int(input("how many elements would you like to add?"))
for i in range(n):
    data=int(input("enter data item:"))
    a_llist.append(data)
print("the linked list is:",end=' ')
a_llist.display()'''
                   
            
                
        

            


                
    
    
    
    

                       
