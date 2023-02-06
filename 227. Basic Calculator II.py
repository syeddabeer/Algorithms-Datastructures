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