#definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
#             print(val1)
#             print(val2)
#             print(carry)
#divmod gives carry and out if numbers are less than 10
            carry, out = divmod(val1 + val2 + carry, 10)    
#             print(carry)
#             print(out)
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next  

# def listprint(self):
#     printval = self.val
#     while printval is not None:
#         print(printval.val)
#         printval = printval.next

#declaring first list node - 243
e3=ListNode(3, None)
e2=ListNode(4, e3)
l1=ListNode(2, e2)

#declaring second list node - 564
f3=ListNode(4, None)
f2=ListNode(6, f3)
l2=ListNode(5, f2)

obj=Solution()

#expeted output - 807
x=obj.addTwoNumbers(l1, l2)

while x is not None:
    #value
    print(x.val)
    #pointer to next
    x=x.next