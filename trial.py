class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value 
        self.next = tail 

class LinkedList:
    def __init__(self, *start):
        self.head = None 
        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        self.head = LinkedNode(value, self.head)

    def pop(self):
        if self.head is None:
            raise Exception("Null")

        val = self.head.value 
        self.head = self.head.next
        return val

        def remove(self, value):
            n = self.head 
            last = None 
            while n != None:
                if n.value == value:
                    if last == None:
                        self.head = self.head.next
                    else:
                        last.next = n.next
                    return True

                last = n
                n = n.next
            return False
