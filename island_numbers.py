
from typing import List

class Solution:

    def dfs(self, grid, cur_i, cur_j) -> int: #递归
        grid[cur_i][cur_j]=0 #很重要的初始化，查看过为1的元素要马上置为0，否则会重复迭代 #关键点，这样就能通过递归不用返回值的方式记录岛数量
        nr,nc=len(grid),len(grid[0])
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]: #di是行方向0 0 1 -1，dj是列方向1 -1 0 0 必须满足当di为0时，dj才能移动，当di为0时，di才能移动
            next_i,next_j=cur_i+di,cur_j+dj
        # for next_i,next_j in [(cur_i-1,cur_j),(cur_i + 1,cur_j),(cur_i ,cur_j-1),(cur_i ,cur_j+1)]:
            if 0<=next_i<nr and 0<=next_j<nc and grid[next_i][next_j]==1: #判断为岛的区域针对边界
                self.dfs(grid,next_i,next_j)

    def max_Area(self,grid:List[List[int]])->int:
        nr=len(grid)
        if nr==0:
            return 0
        nc=len(grid[0])

        num_lands=0
        for y_row in range(nr):
            for x_column in range(nc):
                if grid[y_row][x_column]==1: #判断为岛的区域
                    num_lands+=1
                    self.dfs(grid,y_row,x_column)

        return num_lands

if __name__ == '__main__':
    #4*5
    grid=[[1,1,0,0,1,0],
          [1,0,0,0,0,1],
          [0,0,1,1,1,1],
          [0,0,0,1,1,0]]

    result=Solution().max_Area(grid) #注意调用类时要加上()
    print(result)

