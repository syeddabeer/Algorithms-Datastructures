#depth first search
#algorithm
#number of islands problem
class Solution(object):
    def numIslands(self, grid):
        islands=0;
        #outer loop - row search - len(list)
        for i in range(len(grid)):
            #inner loop - column by column search in a row - len(list[0])
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    #print("counted")
                    islands = islands + 1 #islands += 1
                    self.consecutiveOnes(i,j,grid)
        return islands
    
    def consecutiveOnes(self,i,j,grid):
        #print(str(i)+" "+str(j))
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j]=="0":
            return
        else:
            grid[i][j]="0"
        self.consecutiveOnes(i,j+1,grid)
        self.consecutiveOnes(i,j-1,grid)
        self.consecutiveOnes(i+1,j,grid)
        self.consecutiveOnes(i-i,j,grid)   

# time: O(N^2)
# space: O(min(M,N))

#2d list
# grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
#2d list
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
grid = [
  ["1","1","1"],
  ["0","1","0"],
  ["1","0","0"],
  ["1","0","1"]
]
print(Solution().numIslands(grid))