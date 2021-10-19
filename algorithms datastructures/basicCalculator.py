class Solution:
    def calculate(self, s):
        num, ope, stack = 0, '+', []
        
        for cnt, i in enumerate(s):
            print(cnt, " ", i)
            
            if i.isnumeric():
                num=num*10+int(i)
                print("num ", num)
                
            if i in '+-*/' or cnt==len(s)-1:
                if ope == '+':
                    stack.append(num)
                    print(stack)
                    
                if ope == '-':
                    stack.append(-num)
                    print(stack)
                    
                if ope == '*':
                    temp=stack.pop()*num
                    stack.append(temp)
                    print(stack)
                    
                if ope=='/':
                    temp=int(stack.pop()/num)
                    stack.append(temp)
                    print(stack)
                    
                ope=i
                num=0
        return sum(stack)
                
            
            
            
s="32+2*2"
sol=Solution()
sol.calculate(s)