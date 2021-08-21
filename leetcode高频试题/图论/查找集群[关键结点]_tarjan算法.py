"""
参考
https://leetcode-cn.com/problems/critical-connections-in-a-network/solution/python3-tarjansuan-fa-by-yim-6-p5ok/
tarjan 其实就是一种基于深度优先搜索的，用于求解图的连通性问题的算法 （双连通性即强连通）
https://www.bilibili.com/video/BV1Q7411e7bM?p=2&spm_id_from=pageDriver
割点：无向连通图中，某点和连接点的边去掉后，图不再连通   如：a-b-c 中的b把a-c的连通给切割了
桥：...，某边去掉后，...  把a-b之间的边去掉后a不再连通图，该边是桥，如果把b——c之间边去掉后，该图仍然可以通过a-b-d-c连通，所以b——c不是桥
a-b——c
  | /
  d
dfn[x]: DFS中，x实际被访问的时间点，x被访问的越早，dfn[x]越小
low[x]: DFS中，x通过无向边，可回溯到的最早时间点，所以low[x]是会不断被更新的
注意：由于讨论的是无向图，父可以到子，那么子必定可以到父，而子到父这割点是不予处理的
x 是割点有两种case:   parent——x——nex
case1: 非root && 有nex && low[nex]>=dfn[x]  意思是x不是根结点，并且他有儿子结点，
        不等式：low[x]: x的儿子nex经过回溯后，所能回到最早的那个时间点
              dfn[x]: x点本身在深度搜索过程中搜索到被访问的时间点
case2: root && 有nex>=2个儿子
桥：low[父]>dfn[子]
重点：构造的字典结果：（dfn[父],low[子]）
本次： parent=node , node=nex
输入：
4
0 1
1 2
2 0
1 3
"""
import collections
from typing import List

class Solution:
    def criticalConnections(self, n, connections) :
        graph = collections.defaultdict(list)
        #graph: {0:[1,2],1:[0,2,3],2:[1,0],3:[1]}
        # 建图
        for k, v in connections: #构建坐标式的双向结点图
            graph[k].append(v)
            graph[v].append(k)

        res = []  #记录割点（关键点）

        # 记录每个节点当前时间戳和最早时间戳
        dfn = [-1] * n
        low = [-1] * n
        # graph: {0:[1,2],1:[0,2,3],2:[1,0],3:[1]} 即0连接1和2，1连接0和2和3，...
        """tarjan算法"""
        def tarjan(node, parent, depth):
            dfn[node] = depth
            low[node] = depth
            for nex in graph[node]:
                if nex == parent: continue #下一个结点graph[node]不能和上一个结点相同，即不能构成双向的，跳过
                if dfn[nex] == -1:
                    tarjan(nex, node, depth + 1) #递归-结点深度（下一个））
                    # 如果当前节点仍然比子节点小，说明找到桥
                    if dfn[node] < low[nex]:
                        res.append([node, nex])
                # 更新当前节点的最小时间戳
                low[node] = min(low[node], low[nex]) #dfn被改变过的，有一个箭头向上node指向

        tarjan(0, -1, 0)
        return res

while True:
    try:
        n=list(map(int,input().split(" ")))
        row=n[0] #注意没有len()
        nodeList=[[]*2]*row
        for i_row in range(row):
            nodeList[i_row]=list(map(int,input().strip().split(" ")))
        res=Solution().criticalConnections(n[0],nodeList)
        print(res)
        res=str(res).strip("[]").split(',')
        print(''.join(res))
    except:
        break