"""
双重递归
1.区间和---->前缀和
2.区间和的个数---->dp往前探
3.dfs优化，剪枝---->回溯

nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量，即只有初始化函数值第一次进入，之后变化都只能在函数内部循环
return什么都不写与return None相同
直接声明dict={}是需要dict[element] =value 即key-value对应的
而defaultdict，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值

10 5 -3 3 2 null 11 3 -2 null 1
8
输出： 3
"""
import io
import sys
from collections import defaultdict


class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def stringToTreeNode(input):

    inputValues=[s.strip() for s in input.split(" ")]
    print(inputValues)
    root=TreeNode(int(inputValues[0]))
    nodeQueue=[root]
    front=0
    index=1
    while index<len(inputValues):
        node =nodeQueue[front]
        front+=1

        item=inputValues[index]
        index+=1
        if item!="null":
            leftNumber=int(item)
            node.left=TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index>=len(inputValues):
            break

        item = inputValues[index]
        index += 1
        if item!="null":
            rightNumber=int(item)
            node.right=TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Solution:

    def pathSum(self, root,targetSum):

        res=0
        preSum_count=defaultdict(int) #前缀和_频率
        preSum_count[0]=1

        def backTrace(x,cur_preSum):
            nonlocal res
            nonlocal preSum_count
            if x==None: #if not root
                return

            cur_preSum+=x.value
            print(cur_preSum,preSum_count)
            """关键，第一步时要找到差值为1"""
            if (cur_preSum-targetSum) in preSum_count:
                print(cur_preSum-targetSum)
                res+=preSum_count[cur_preSum-targetSum]

            preSum_count[cur_preSum]+=1
            backTrace(x.left,cur_preSum)
            backTrace(x.right, cur_preSum)
            preSum_count[cur_preSum]-=1 #剪枝

        backTrace(root,0)
        return res

def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')
    lines=readlines()

    while True:
        line=next(lines)
        root =stringToTreeNode(line)
        targetSum=int(next(lines))
        res=Solution().pathSum(root,targetSum)
        print(res)

if __name__ == '__main__':
    main()