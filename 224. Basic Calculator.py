class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        num = 0
        curr = 0
        signs = {"+" : 1, "-" : -1, ")": 1}
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-)":
                curr += sign * num
                num = 0
                sign = signs[char]
                if char == ")":
                    curr = stack.pop() * curr + stack.pop()  
            elif char == "(":
                stack.append(curr)
                stack.append(sign)
                curr = 0
                sign = 1
        ##last edge case
        curr += num * sign
        
        return curr


"""
class Solution:
    def calculate(self, s):
        curr=0
        sign=1
        signs={"+":1, "-":-1, ")":1}
        stack=[]
        #"- (3 + (4 + 5))"
        num=0
        print(s)
        for i in s:
            if i.isdigit():
                num = num*10+int(i)
                print(f"digit loop: num={num}")
                
            elif i in "+-)":
                curr+=sign*num
                num=0
                sign=signs[i]               
                
                print(f"+-) loop: curr={curr}\nnum={num}\nsign={sign}")
                if i in ")":
                    curr=stack.pop()*curr+stack.pop()
                    
                    print(f") loop: curr={curr}")
            
            elif i in "(":
                print(f"start ( loop: curr={curr}\nsign={sign}\nstack={stack}")
                stack.append(curr)
                stack.append(sign)
                curr=0
                sign=1
                print(f"end ( loop: curr={curr}\nsign={sign}\nstack={stack}")
        curr+=num*sign
        return curr