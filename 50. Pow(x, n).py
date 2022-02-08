# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Author : dabeeruddin syed
        it is important to handle border cases, brother.
        """
        if n<0:
            x=1/x
            n=-n
            return self.myPow(x,n)
            
        elif n==0 and x==0:
            #return False
            return 1
        
        elif n==0:
            return 1
        
        elif n==1:
            return x
        
        elif x==0:
            return 0
        
        elif x==1:
            return 1
        
        elif n % 2 == 0:
            half=self.myPow(x,n//2)
            return half * half
        
        else:
            half=self.myPow(x,n//2)
            return x * half * half
        
#solution object
solution=Solution()
#cases
solution.myPow(2, -7)
solution.myPow(5, -2)
solution.myPow(5, -1)
solution.myPow(5, 0)
solution.myPow(0, 0)
solution.myPow(25, 1)
solution.myPow(2, 7)
solution.myPow(2, 8)