
from typing import List

class Solution:
    # 1.从一点向四个方向深度优先遍历，计算岛屿总面积
    def dfs(self, grid, cur_i, cur_j) -> int: #递归
        if cur_i<0 or cur_j<0 or cur_i==len(grid) or cur_j==len(grid[0]) or grid[cur_i][cur_j]!=1:
            return False
        grid[cur_i][cur_j]=0
        ans=1
        for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            next_i,next_j=cur_i+di,cur_j+dj

            ans+=self.dfs(grid,next_i,next_j)
        return ans

    # 2.比较每个岛屿面积，取最大值
    def max_Area(self,grid:List[List[int]])->int:
        ans=0
        for k_row,v_row in enumerate(grid):
            for k_col,v_col in enumerate(v_row): #注意是v_row 一行所有的值
                ans=max(ans,self.dfs(grid,k_row,k_col))
        return ans

if __name__ == '__main__':
    #4*5
    grid=[[1,1,0,0,1,0],
          [1,0,0,0,0,1],
          [0,0,1,1,1,1],
          [0,0,0,1,1,0]]

    result=Solution().max_Area(grid) #注意调用类时要加上()
    print(result)

