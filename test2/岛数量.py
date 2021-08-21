class Solution:

    def IslandNums(self, grid):
        if len(grid)==0:
            return 0
        nums=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.CalculateIsland(grid,i,j)
                    nums+=1
        return nums

    def CalculateIsland(self, grid, cur_i, cur_j):

        grid[cur_i][cur_j]=0
        nr, nc = len(grid) - 1, len(grid[0]) - 1 #因为下面的for循环里面是[1,0],[-1,0]中1和-1开头，不是0，所以需要-1
        for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            next_i,next_j=cur_i+di,cur_j+dj
            if 0<=cur_i<nr and 0<=cur_j<nc and grid[next_i][next_j]==1:
                self.CalculateIsland(grid,next_i,next_j)

if __name__ == '__main__':
    #4*5
    grid=[[1,1,0,0,1,0],
          [1,0,0,0,0,1],
          [0,0,1,1,1,1],
          [0,0,0,1,1,0]]

    result=Solution().IslandNums(grid)
    print(result)