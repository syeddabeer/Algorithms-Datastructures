# Dabeeruddin Syed # Doubly linked list # Bi-directional linked list

class LinkedNode(object):
    # Each node has its value and a pointer that points to next node in the Linked List
    def __init__(self, value, next = None, previous = None):
        self.value = value;
        self.next = next;
        self.previous = previous

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    # for inserting at the beginning of linked list
    def insertAtStart(self, value):
        if self.head == None:
            self.head = LinkedNode(value)
        else:
            newNode = LinkedNode(value)
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

    # for inserting at the end of linked list
    def insertAtEnd(self, value):
        newNode = LinkedNode(value)
        # start from head and traverse along the list
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp

    # deleting a node from linked list
    def delete(self, value):
        temp = self.head
        # null linked list 
        if (temp == None):
            return

        if(temp.next != None):
            # if head node is to be deleted
            if(temp.value == value):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.value == value):
                        break
                    temp = temp.next
                if(temp.next):
                    # if element to be deleted is in between
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # if element to be deleted is the last element
                    temp.previous.next = None
                    temp.previous = None
                return



    # for printing the contents of linked lists
    def printdll(self):
        temp = self.head
        while(temp != None):
            print(temp.value, end=' ')
            temp = temp.next

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(2)
    dll.insertAtEnd(3)
    dll.insertAtStart(4)
    dll.printdll()
    dll.delete(2)
    print()
    dll.printdll()
