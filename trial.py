from threading import Condition
class BoundededBlockingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = []
        self.c1 = Condition()
        self.c2 = Condition()

    def enqueue(self, element):
        with self.c1:
            self.c1.wait_for(lambda: len(self.q)<self.capacity)
            self.q.append(element)
            self.c1.notify_all()

    def dequeue(self):
        with self.c2:
            self.c2.wait_for(lambda: len(self.q)>0)
            self.q.pop(0)
            self.c2.notify_all()

    def size(self):
        return len(self.q)

1
1
["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
[[2],[1],[],[],[0],[2],[3],[4],[]]

[2, 1]