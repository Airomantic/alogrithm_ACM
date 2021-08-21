
"""
prim算法
https://leetcode-cn.com/problems/optimize-water-distribution-in-a-village/
最小生成树 Minimum Spanning Tree ，所有权重之和最小（举例：城市多个区点光缆铺设成本最低）
1.没有环
2.所有的结点Vertices都相连
3.N Vertices,N-1 Edges
输入：
3
[1,2,2]
[[1,2,1],[2,3,1]]
输出：
3
https://www.bilibili.com/video/BV1Eb41177d1?from=search&seid=8769610283956528193
Kruskal：直接选择那些权值最小的边              1.先排序  2.再从小到大把边放入结点中，出现环的边去掉
Prim：从顶点出发优先选择连接两个顶点集合所有边中权重最小的边，一集合是已选的，另一集合是未选的
        1.Update    如果连接边的权重小于对应顶点列表表中的值，则更新列表值为该边的权重，同时更新父亲列表以记录该边，反之则不变
        2.Scan      扫描最小距离列表，找到最小值所对应的顶点，该最小值就是前面提到所有连接两个顶点集合中最小权重边的值
        3.Add       添加上一步找到的最小值的顶点到已选顶点集合中，同时按照父亲列表信息，创建最小生成树的一条边
        循环：       接着，以该顶点为新的目标顶点重复第一步操作
        |node    |     1      2      3
        |selected|
        |minDist |
        |parent  |
parent是node的前一个结点
"""
import heapq
import io
import json
import sys
from collections import defaultdict

class Solution:
    #n表示n栋房子
    def minCostToSupplyWater(self, n, wells, pipes):
        # edges=[1,2,2],[2,3,1],[0,1,1],[0,2,2],[0,3,2]] 由wells权重接入放在后三行的第三列
        edges = pipes
        for i, w in enumerate(wells):
            edges.append([0, i + 1, w]) #

        adjvex = defaultdict(lambda: defaultdict(lambda: float('inf')))  # 初始化无穷大二维字典

        for x, y, w in edges:
            """防止2点中间有多条边"""
            adjvex[x][y] = min(adjvex[x][y], w)  #不过是x->y还是y->x，都选择最小的那个权重是一样的，这样就变成无向单边的了
            adjvex[y][x] = min(adjvex[y][x], w)


        # ------------ prim算法求MST ------------#
        res = 0
        minHeap = []
        MST = set() #MST={0,1,2,3}
        heapq.heappush(minHeap, (0, 0)) #初始化，函数化的意思，即将右边的压入左边声明的[]最小堆里面

        while minHeap and len(MST) < n + 1:
            cost, x = heapq.heappop(minHeap)
            if x in MST:
                continue

            MST.add(x)
            res += cost
            """将adjvex后两列值压入最小堆，借用最小堆构造最小生成树（权重之和最小）"""
            for y, w in adjvex[x].items():
                heapq.heappush(minHeap, (w, y))  #cost=w

        return res

def stringToIntegerList(input):
    return json.loads(input)

def readlines():
    for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
        yield lines.strip('\n')


if __name__ == '__main__':
    lines = readlines()
    while True:
        # n = int(input())
        # wells = list(map(int, input().strip().split(" ")))
        n=int(next(lines))
        wells=stringToIntegerList(next(lines))
        pipes = stringToIntegerList(next(lines))
        res = Solution().minCostToSupplyWater(n, wells, pipes)
        print(res)