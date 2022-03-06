#1188. Design Bounded Blocking Queue
from threading import Condition
class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.q = []
        self.capacity = capacity
        self.c1 = Condition()
        self.c2 = Condition()
        

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        with self.c1:
        	self.c1.wait_for(lambda: len(self.q) < capacity)
        	self.q.append(element)
        	self.c1.notify_all()
        

    def dequeue(self):
        """
        :rtype: int
        """
        with self.c2:
        	self.c2.wait_for(lambda: len(self.q) > 0)
        	self.q.pop(0)
        	self.c2.notify_all()
        

    def size(self):
        """
        :rtype: int
        """
        return len(self.q)



# METHOD 2 - without inbuilt. linked list and Condition() only
import threading

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class BoundedBlockingQueue(object):
   
    def __init__(self, capacity):
        self.__front = self.__rear = None
        self.__size = 0
        self.__capacity = capacity
        self.__enq_cv = threading.Condition()
        self.__dq_cv = threading.Condition()
        
    def enqueue(self, element):
        with self.__enq_cv:
            while self.is_full():
                self.__enq_cv.wait()
        
        node = Node(element)
        with self.__dq_cv:
            if self.__rear:
                self.__rear.next = node
            else:
                self.__front = node
            self.__rear = node
            self.__size += 1
            self.__dq_cv.notify()
        

    def dequeue(self):
        with self.__dq_cv:
            while self.is_empty():
                self.__dq_cv.wait()
        
            with self.__enq_cv:
                node_to_dq = self.__front
                dq_value = self.__front.value
                if self.__front == self.__rear:
                    self.__front = self.__rear = None
                else:
                    self.__front = self.__front.next
                del node_to_dq
                self.__size -= 1
                self.__enq_cv.notify()
                return dq_value
                
    def size(self):
            return self.__size
    
    def is_full(self):
        return self.__size == self.__capacity
    
    def is_empty(self):
        return self.__size() == 0

"""
Implement a thread-safe bounded blocking queue that has the following methods:

BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
int size() Returns the number of elements currently in the queue.
Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only makes calls to the enqueue method or a consumer thread that only makes calls to the dequeue method. The size method will be called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview.

Example 1:
Input:
1
1
["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
[[2],[1],[],[],[0],[2],[3],[4],[]]

Output:
[1,0,2,2]

Explanation:
Number of producer threads = 1
Number of consumer threads = 1

BoundedBlockingQueue queue = new BoundedBlockingQueue(2);   // initialize the queue with capacity = 2.

queue.enqueue(1);   // The producer thread enqueues 1 to the queue.
queue.dequeue();    // The consumer thread calls dequeue and returns 1 from the queue.
queue.dequeue();    // Since the queue is empty, the consumer thread is blocked.
queue.enqueue(0);   // The producer thread enqueues 0 to the queue. The consumer thread is unblocked and returns 0 from the queue.
queue.enqueue(2);   // The producer thread enqueues 2 to the queue.
queue.enqueue(3);   // The producer thread enqueues 3 to the queue.
queue.enqueue(4);   // The producer thread is blocked because the queue's capacity (2) is reached.
queue.dequeue();    // The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
queue.size();       // 2 elements remaining in the queue. size() is always called at the end of each test case.
Example 2:

Input:
3
4
["BoundedBlockingQueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","enqueue"]
[[3],[1],[0],[2],[],[],[],[3]]
Output:
[1,0,2,1]

Explanation:
Number of producer threads = 3
Number of consumer threads = 4

BoundedBlockingQueue queue = new BoundedBlockingQueue(3);   // initialize the queue with capacity = 3.

queue.enqueue(1);   // Producer thread P1 enqueues 1 to the queue.
queue.enqueue(0);   // Producer thread P2 enqueues 0 to the queue.
queue.enqueue(2);   // Producer thread P3 enqueues 2 to the queue.
queue.dequeue();    // Consumer thread C1 calls dequeue.
queue.dequeue();    // Consumer thread C2 calls dequeue.
queue.dequeue();    // Consumer thread C3 calls dequeue.
queue.enqueue(3);   // One of the producer threads enqueues 3 to the queue.
queue.size();       // 1 element remaining in the queue.

Since the number of threads for producer/consumer is greater than 1, we do not know how the threads will be scheduled in the operating system, even though the input seems to imply the ordering. Therefore, any of the output [1,0,2] or [1,2,0] or [0,1,2] or [0,2,1] or [2,0,1] or [2,1,0] will be accepted.
"""