"""
这题可以使用   并查集+tarjan算法

仔细思考我们会发现最终的答案不可能超过 2。因为对于 n×m 的岛屿（n,m≥2），我们总是可以将某个角落相邻的两个陆地单元变成水单元，
从而使这个角落的陆地单元与原岛屿分离。而对于 1×n 类型的岛屿，我们也可以选择一个中间的陆地单元变成水单元使得陆地分离。
因此最终的答案只可能是 0,1,2。
那么我们只要依次检查 0 或 1 的答案是否存在即可。
⓵0 的情况对应于一开始的二维网格已经是陆地分离的状态，
②而对于 1 的情况，我们只要枚举每一个存在的陆地单元，将其修改为水单元，再去看是否为陆地分离的状态即可。
关键点：如果都不能变为陆地分离的状态，那么答案即为 2。（省去了考虑的计算）
策略：最后要解决的即为②「如何判断二维网格是否为陆地分离的状态」。根据其定义，我们可以知道只要统计全部为 1 的四连通块数量是否大于 1 即可，
统计连通块数量可以通过深度优先搜索来处理。
https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island/solution/python-dfs-by-wzhaooooo/
# dfs三种情况
        # 1) 全是水或岛屿个数大于1: 0天
        # 2) 去除掉一个陆地后岛屿个数大于1或为0: 1天
        # 3) 总能找到一个岛屿的角或是连接处将其分离: 2天
"""

class Solution:

    def minDays(self,grid):
        _dir_ = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Solution类中的全局变量
        row, col = len(grid), len(grid[0])  # Solution类中的全局变量

        def DFS(cur_i, cur_j, used):
            for di, dj in _dir_:
                next_i, next_j = cur_i + di, cur_j + dj
                if 0<=next_i<len(grid) and 0<=next_j<len(grid[0]):
                    if used[next_i][next_j] == 1 or grid[next_i][next_j] == 0:
                        continue
                    """used==0和grid==1的"""
                    used[next_i][next_j] = 1 #该深度优先就是处理used周围变成陆地的，也就是把grid陆地的地方used对应记为陆地
                    DFS(next_i, next_j, used)

        def CalCount(grid):
            ans=0
            # used=[[0]*col]*row #错误🙅🤔
            used=[[0]*col for i in range(row)] #注意这里的used没循环经历一次都会全部变成0
            # used=[[0 for i in range(col)] for j in range(row)] #也可
            # print(used)
            for i in range(row):
                for j in range(col):
                    """关键点：用used记住grid这个某处陆地的坐标点"""
                    if grid[i][j]==1 and used[i][j]==0: #注意这里是and,一定不要写成or
                        used[i][j]=1
                        DFS(i,j,used) #直到判断used仍然有水的ans就加1，这样就能判断出连通的地点了，同时该处记为陆地避免下次重复访问
                        ans+=1
            return ans

        """第一种情况"""
        island_num=CalCount(grid) #等于0的情况是grid==0全是水 或者 要两次以上DFS处理才能使得used全是1这种可能就是grid全是1
        # print("test finally")
        if island_num==0 or island_num>1:#全是0或全是1
            return 0
        """第二种情况"""
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    grid[i][j]=0
                    island_num=CalCount(grid) #used在第一次调用时已经计算记录的连通数量
                    if island_num==0 or island_num>1:
                        return 1
                    grid[i][j]=1 #恢复
        """第三种情况"""
        return 2 #否则返回2


if __name__ == '__main__':
    while True:
        try:
            n=list(map(int,input().split(" ")))
            row,col=n[0],n[1]
            grid=[[]*col]*row
            for i_col in range(row):
                grid[i_col]=list(map(int,input().split(" ")))
            # print(grid)
            res=Solution().minDays(grid)
            print(res)
        except:
            break
