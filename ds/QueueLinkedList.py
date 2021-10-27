"""
    Demonstration of Queue using Linked Lists.
    First In First Out
    Queue
    Author: Dabeeruddin Syed
"""

class LinkedNode:
    def __init__(self, value, tail = None):
        self.value = value
        self.next = tail
    
    def checkInfinite(self):
        """Check whether infinite loop via next."""
        p1 = p2 = self
        while p1 != None and p2 != None:
            if p2.next == None: return False

            p1 = p1.next
            p2 = p2.next.next
            
            if p1 == p2: return True
        return False

# elements are added to the right which is the tail
# elements are removed from the left which is the head
# tail-head   value-next  value-next  value-next

class QueueLinkedList:
    def __init__(self, *start):
        """Demonstrate queue using linked list in Python."""
        self.head = None
        self.tail = None
        for _ in start:
            self.append(_)

    def append(self, value):
        """Add value to end of queue."""
        newNode = LinkedNode(value, None)
        if self.head is None:                       # no elements
            self.head = self.tail = newNode
        else:                                   # already contain elements
            self.tail.next = newNode
            self.tail = newNode

    def isEmpty(self):
        """Determine if queue is empty."""
        return self.head == None

    def pop(self):
        """Remove first value from queue."""
        if self.head is None:
            raise Exception ("Queue is empty.")
        val = self.head.value
        self.head = self.head.next
        if self.head is None:              # removing an element makes a queue empty (None)
            self.tail = None
        return val

    def __iter__(self):
        """Iterator of values in queue."""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
        
    def __repr__(self):
        """String representation of queue."""
        if self.head is None:
            return 'queue:[]'

        return 'queue:[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        """Count values in queue."""
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count


q = QueueLinkedList()
q.append(1)
q.append(2)
q.append(3)
print(q)

# already present implementations
# from collections import deque