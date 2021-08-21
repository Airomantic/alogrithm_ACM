
from typing import List

class Solution:
    # 1.从一点向四个方向深度优先遍历，计算岛屿总面积
    def dfs(self, grid, cur_i, cur_j) -> int: #递归
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:  # 关键点1 判断前进一位这块是不是岛屿，如果是岛屿就向下执行
            return 0 #注意最后一个条件grid[cur_i][cur_j] != 1
        ans = grid[cur_i][cur_j] #写1 也可以格子是数值几就对应几
        grid[cur_i][cur_j] = 0  # 初始化为0，还没遇到岛屿的时候，同时#之后被访问过的陆地设为0，不然计算机会一直持续运行下去
          # 关键点2 每次计数加几 ，这里遇到一个小块，一次当然加1了
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj # 向->上下右左
            ans += self.dfs(grid, next_i, next_j)  # 关键点3 遇到岛屿“1”，就加1，实现递归
        return ans
    # 2.比较每个岛屿面积，取最大值
    def max_Area(self,grid:List[List[int]])->int:
        ans=0
        #这个循环是出发点
        print(grid)
        for k_row,v_row in enumerate(grid): #key-value
            for k_column,v_column in enumerate(v_row): #这个row就相当于grid[0]，只不过里面的0由row控制
                #作用就是取坐标而已，这样才能在接下来进行四个方向的深度遍历
                ans = max(self.dfs(grid, k_row, k_column), ans)  # 传入二维list进行面积计算，逐个比较出最大值

        return ans

if __name__ == '__main__':
    #4*5
    grid=[[1,1,0,0,1,0],
          [1,0,0,0,0,1],
          [0,0,1,1,1,1],
          [0,0,0,1,1,0]]

    result=Solution().max_Area(grid) #注意调用类时要加上()
    print(result)

