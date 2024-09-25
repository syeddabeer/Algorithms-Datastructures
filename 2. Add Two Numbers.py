"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

1. Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

class Solution:
  def addTwoNumbers(self, l1, l2):
    dummyHead = ListNode(0)
    curr = dummyHead 
    carry = 0
    
    while l1 != None or l2!= None or carry != 0:
        
        l1Val = l1.val if l1 else 0 
        l2Val = l2.val if l2 else 0
        
        columnSum = l1Val + l2Val + carry 
        carry = columnSum // 10 
        
        newNode = ListNode(columnSum%10)
        curr.next = newNode 
        curr = newNode
        
        l1 = l1.next if l1 else None 
        l2 = l2.next if l2 else None 
    
    return dummyHead.next
