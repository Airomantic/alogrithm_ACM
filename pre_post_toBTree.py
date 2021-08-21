import io
import json
import sys
from typing import List
"""
输入：
1 2 4 5 3 6 7
4 5 2 6 7 3 1
输出：[1,2,3,4,5,6,7]
"""


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution: #注意这里不要有括号
    def constructFromPrePost(self,pre: List[int],post:List[int]):
        if not pre:
            return None
        root = TreeNode(pre[0])  # 根结点，注意TreeNode类没有单独设置根赋值，所以不能写成TreeNode(0)
        if len(pre) == 1:
            return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])  # 前序跳过第一位（根结点），后序不需要跳过，但最后一个是根结点不用遍历
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-2])  # 这里postorder[L:-1]到-2或-1似乎对结果都没有影响

        return root

def TreeNodeToString(root): #利用队列
    if not root:
        return '[]'
    output=""
    current=0
    Queue=[root]
    while current != len(Queue):
        node=Queue[current]
        current+=1

        if not node:
            output += "null, "
            continue

        output+= str(node.value) + ", " #注意这里是node.val
        Queue.append(node.left)
        Queue.append(node.right)
    return "["+output[:-2]+"]"


def listToTreeNode(input):
    inputValues=[s.strip() for s in input.split()]
    root=TreeNode(int(inputValues[0]))
    nodeQueue=[root]
    front=0
    index=1
    while index<len(inputValues):
        node =nodeQueue[front]
        front+=1

        item = inputValues[index]
        index+=1
        if item!="null":
            leftNumber=int(item)
            node.left=TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index>=len(inputValues):
            break

        item = inputValues[index]
        index += 1
        if item != "null":
            rightNumber=int(item)
            node.right=TreeNode(rightNumber)
            nodeQueue.append(node.right)

    return root

def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')
            
    lines=readlines()
    while True:

        line = next(lines)
        pre=listToTreeNode(line)
        line2 = next(lines)
        post = listToTreeNode(line2)
        TN=Solution().constructFromPrePost(pre,post)
        result=TreeNodeToString(TN)
        print(result)



if __name__ == '__main__':
    EnterMain()