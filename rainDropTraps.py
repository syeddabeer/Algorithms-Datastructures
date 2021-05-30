#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
class waterTrap:
    #[0,1,0,2,1,0,1,3,2,1,2,1]
    def func(self, list):
        #left pointer that moves
        leftidx=0
        #right pointer that is fix
        rightidx=len(list)-1
        # max in the left region to pointer
        leftmax=0
        # max in the right region to pointer
        rightmax=0
        # return value to raindrops
        raindrops=0
        # logic: raindrops is min(leftmax,rightmax)-self.height. if this is negative, this should be zero.
        while leftidx <= rightidx:
            leftmax  = max(list[0:leftidx]) if leftidx else 0
            rightmax = max(list[leftidx:])
            temp = min(leftmax, rightmax) - list[leftidx]
            raindrops += max(0, temp)
            #print(raindrops)
            leftidx+=1
        return raindrops

list=[0,1,0,2,1,0,1,3,2,1,2,1]
print(waterTrap().func(list))

list2=[1,0,3]
print(waterTrap().func(list2))