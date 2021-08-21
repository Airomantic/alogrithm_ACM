"""
https://leetcode-cn.com/problems/path-sum-iii/solution/437zhi-xu-yi-ci-di-gui-wu-xing-dai-ma-yong-lie-bia/

10 5 -3 3 2 null 11 3 -2 null 1
10 5 3 2 2 2 5
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
    if not input:
        return None
    inputValues=[s.strip() for s in input.split()]
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
    """返回root，记得写到while外面"""
    return root

class Solution:

    def pathSum(self, root,targetSum):

        def dfs(root, sumList):
            if root is None: #当继续深入时没有子结点，sumList则返回上一次加root.value之前的状态
                return 0
            sumList=[num+root.value for num in sumList] #记录每一步的和，即之前的list元素分别加上新的root.value
            sumList.append(root.value) #再记录刚才加的那个值是多少

            count=0
            for num in sumList:
                if num==targetSum:
                    count+=1 #频率，这里的count会被count=0覆盖
            # 这里的count会记录每一分枝（左右孩子）得到targetSum的次数
            return count+dfs(root.left,sumList)+dfs(root.right,sumList) #这个count+就像DFS记录岛的数量一样

        return dfs(root,[]) #返回count答案

    def inorderTraversal(self, root):
        """中序"""
        res = []

        def DFS(root):
            if not root:
                return
            DFS(root.left)
            res.append(root.value)
            DFS(root.right)

        DFS(root)
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