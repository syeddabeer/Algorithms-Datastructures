class LinkedNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next 
        self.previous = previous

class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def insertAtStart(self, value):
        if self.head == None:
            self.head = LinkedNode(value)
        else:
            newNode = LinkedNode(value)
            newNode.next = self.head 
            self.head.previous = newNode
            self.head = newNode

    def insertAtEnd(self, value):
        newNode = LinkedNode(value)

        temp = self.head 
        while temp.next != Node
            temp=temp.next 
        temp.next = newNode


    def delete(self, value):