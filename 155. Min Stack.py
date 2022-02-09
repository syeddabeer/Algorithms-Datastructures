class MinStack():
    def __init__(self):
        self.stack=[]
    
    def push(self, x):
        if not self.stack:
            self.stack.append((x,x))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((x, min(x, current_min))) #current_min is stack[-1][1]
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]
        
    def getMin(self):
        return self.stack[-1][1]
        
    
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""