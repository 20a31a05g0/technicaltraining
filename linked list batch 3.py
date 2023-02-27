class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        if not temp:
            print('List is empty. ')
            return
        else:
            print('start: ',end=' ')
        while(temp):
            print(temp.data, end=' -> ')
            temp=temp.next
        print('end. ')
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        elif self.head.data >= new_node.data:
            new_node.next=self.head
            self.head=new_node
        else:
            #location the node before insertion point
            current=self.head
            while current.next and new_node.data > current.next.data:
                current=current.next
            #insetion
            new_node.next=current.next
            current.next=new_node
    def delete(self,key):
        if self.head is None:
            print('deletion error: THE LIST ID EMPTY..')
            return
        if self.head.data==key:
            self.head=self.head.next
            return
            #find the position of first occurance of the key
        current=self.head
        while current:
            if current.data==key:
                break
            previous=current
            current=current.next
        if current is None:
            print('deletion error: Key not found.')
        else:
            previous.next=current.next
#__name__ is python special variable
if __name__=='__main__':
    #create an object
    LL=LinkedList()
    print('')
    #Insert some Nodes
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)

    LL.printList()
    LL.delete(12)
    LL.delete(8)
    LL.delete(11)
    LL.printList()
    
