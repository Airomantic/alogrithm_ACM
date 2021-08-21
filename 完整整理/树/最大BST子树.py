import io
import json
import sys
"""
10 5 15 1 8 null 7

"""


class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


def stringToTreeNode(input): #这里的input只能通过sys.stdin流才好转化成list处理
    if not input:
        return None
    inputValues=[s.strip() for s in input.split()] #去除分割符的同时转化成list
    print(inputValues)
    root=TreeNode(int(inputValues[0])) #当判断到null时，是不会放进int去的
    nodeQueue=[root]
    front=0
    index=1
    while index<len(inputValues):
        node=nodeQueue[front]
        front+=1

        item=inputValues[index]
        index+=1
        if item!="null":
            leftNumber=int(item)
            node.left=TreeNode(leftNumber) #这个leftNumber就是node.value，然后用node.left指向TreeNode结构中的这个父值
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

    def largestBSTSubtree(self, root):
        def helper(root):
            if not root:
                return float('inf'),float('-inf'),0
            left_min,left_max,left_len=helper(root.left)
            right_min, right_max, right_len = helper(root.right)

            """题意条件：左<node.value<右：左子树中的最大值<父值<右子树中的最小值"""
            if left_max<root.value<right_min:
                return min(root.value,left_min),max(root.value,right_max),left_len+right_len+1 #第一二参数交换位置和第三个参数的每轮结果输出
            return float('-inf'),float('inf'),max(left_len,right_len) #注意负号-别写成=

        return helper(root)[2]


def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    # while True:
    #     try:
    # input() #如果智障的牛客网非要你输入一个n来限制list长度，就设个无用的input()，来躲过测试用例
    line=next(lines)
    root=stringToTreeNode(line)
    res=Solution().largestBSTSubtree(root)
    print(res)
        # except:
        #     break


if __name__ == '__main__':
    main()