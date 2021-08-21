
"""
输入：
5 5
1 2 3 0 0
1 2 0 1 0
0 1 0 2 0
0 0 0 0 0
1 0 2 0 0
输出：
10
"""

class Solunion:

    def dfs(self, grid, cur_i, cur_j):
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] <1:  # 关键点1 判断前进一位这块是不是岛屿，如果是岛屿就向下执行
            return 0
        ans = grid[cur_i][cur_j]
        grid[cur_i][cur_j]=0 #别写成双等号了
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i,next_j=cur_i+di,cur_j+dj
            ans+=self.dfs(grid,next_i,next_j)
        return ans

    def maxArea(self, grid):
        ans = 0
        for k_row,v_row in enumerate(grid):
            for k_col,v_col in enumerate(v_row):
                ans=max(self.dfs(grid, k_row, k_col),ans)
        return ans


if __name__ == '__main__':
    n = list(map(int, input().split(" ")))
    num = [[] * n[0]] * n[0]
    for row in range(n[0]):
        num[row] = list(map(int, input().split(" ")))

    ans=Solunion().maxArea(num)
    print(ans)