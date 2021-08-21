"""
这题可以使用   并查集+tarjan算法

"""
from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1 for x in range(n)]
        self.size = [1 for x in range(n)]

    def Find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        return True


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # -------------------------- 最多2步，找个角落就可轻松隔离1个角点 -------------------------------#
        # --------------------- 通过并查集，计算出有几个连通域 --------------------#
        Row, Col = len(grid), len(grid[0])
        UF = UnionFind(Row * Col)
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1:  # 陆地
                    xID = r * Col + c
                    if UF.parent[xID] == -1:
                        UF.parent[xID] = xID  # 正式加进并查集
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < Row and 0 <= nc < Col and grid[nr][nc] == 1:  # 也是陆地
                            yID = nr * Col + nc
                            if UF.parent[yID] == -1:
                                UF.parent[yID] = yID  # 正式加进并查集
                            UF.Union(xID, yID)

        part = sum(UF.parent[x] == x for x in range(Row * Col))
        if part == 0 or part > 1:
            return 0

        # 连通域为1.是个无向连通图。再上tarjan算法，找割点
        # --------------------- tarjan 找割点 ---------------------------------#
        adjvex = defaultdict(set)  # 邻接表
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1:
                    xID = r * Col + c
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < Row and 0 <= nc < Col and grid[nr][nc] == 1:  # 也是陆地
                            yID = nr * Col + nc
                            adjvex[xID].add(yID)
                            adjvex[yID].add(xID)

        dfn = [0 for _ in range(Row * Col)]  # dfs中被访问的实际时间
        low = [0 for _ in range(Row * Col)]  # dfs中通过无向边可以往前回溯到的最早的时间节点
        self.T = 1  # 全局时钟
        self.find = False

        def tarjan(x: int, parent: int) -> None:
            dfn[x] = self.T
            low[x] = self.T  # 初始化
            self.T += 1
            child = 0  # 几个儿子
            for y in adjvex[x]:
                if dfn[y] == 0:  # y还未访问过
                    child += 1
                    tarjan(y, x)  # 继续递归，dfs
                    low[x] = min(low[x], low[y])

                    if parent == -1 and child >= 2:  # x是root，且有2个以上的孩子 x是root，是割点
                        self.find = True
                    elif parent != -1 and low[y] >= dfn[x]:  # 可以回溯的最早时间点比父节点晚，x就是割点
                        self.find = True
                else:  # y访问过了
                    if y != parent:  # 且y不是x的父亲
                        low[x] = min(low[x], dfn[y])

        for x in range(Row * Col):
            if UF.parent[x] != -1:  # 是陆地
                if UF.size[UF.Find(x)] == 1:  # 只有一块陆地的情况。是无法找割点的
                    return 1
                tarjan(x, -1)
                break
        if self.find == True:
            return 1
        return 2


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
