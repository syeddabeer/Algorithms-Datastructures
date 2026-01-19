class Solution:
    def calculate(self, s):
        num, ope, stack = 0, '+', []
        #s="32+2*2"        
        for cnt, i in enumerate(s):
            # print(cnt, " ", i)
            if i.isnumeric():
                num=num*10+int(i) 
            if i in '+-*/' or cnt==len(s)-1:
                if ope == '+':
                    stack.append(num) 
                if ope == '-':
                    stack.append(-num)
                if ope == '*':
                    temp=stack.pop()*num
                    stack.append(temp)
                if ope=='/':
                    temp=int(stack.pop()/num)
                    stack.append(temp)
                ope=i
                num=0
            print("stack: ", stack)
        return sum(stack)          
 # time: O(N)
 #space: O(1)           
            
            
s="32+2*2"
sol=Solution()
sol.calculate(s)

"""
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5
""""