class Solution:
    def reverse(self, x: int) -> int:
        mina = -2**31
        maxb = 2**31 - 1
        if x not in range(mina, maxb): #handle bufferflow
            return 0
        elif x >= 0:
            a = int(str(x)[::-1])
            return a
        else:
            a = int(str(x*-1)[::-1])
            return a*-1