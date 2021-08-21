import io
import json
import sys
"""
#元组形式（值和下标一一对应）
#要注意判空
"""

def stringToIntegerList(input):
    return json.loads(input)

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def stringToTreeNode(input):
    input=input.strip() #用于去除首位的字符，不写则为去除首尾的空格（如果有空格的话）
    input=input[1:-1]
    if not input:
        return None
    inputValues=[s.strip() for s in input.strip(',')] #注意这个中括号，此时传入[values]中括号到inputValues数组里面，之后index需要从1开始取值
    root=TreeNode(int(inputValues[0])) #初始化
    nodeQueue=[root] #声明构造一个list表示队列，所以root外面有个中括号，这个root类似一个哑结点,以便最后通过它返回所有的值
    front=0 #相当于current
    index=1
    while index<len(inputValues):
        node=nodeQueue[front] #有了之前的nodeQueue=[root]，这里才好生成对头
        front=front+1

        item_left=inputValues[index]
        index=index+1
        if item_left != "null":
            leftNumber=int(item_left) #注意判空，因为这个有些是没有结点的
            node.left=TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index>=len(inputValues):#注意这里的防止溢出判断放在while里面
            break

        item_right=inputValues[index]
        index=index+1  #这里还是用到了的，注意return root 在while外面
        if item_right != "null":
            rightNumber=int(item_left)
            node.right=TreeNode(rightNumber)
            nodeQueue.append(node.right)

    return root

class Solution:
    def averageOflevels(self,root:TreeNode):

        def DFS(root:TreeNode,level:int):
            if not root:
                return #跟None一样
            if level<len(numbersSum):
                numbersSum[level]=root.val
                count[level]+=1
            else:
                numbersSum.append(root) #目的：遇到父结点即将往深下
                count.append(1) #每一层多一个元素，当层加1
            DFS(root.left,level+1)
            DFS(root.right,level+1)

        numbersSum = list()
        count = list()
        DFS(root,0) #从根结点，值和下标开始
        return [numbersSum/count for numbersSum,count in zip(numbersSum,count)]

def EnterMain():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield line.strip('\n')
    lines=readlines()
    while True:
        try:
            line=next(lines)
            LN=stringToTreeNode(line)
            result=Solution().averageOflevels(LN)
            out=str(result)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    EnterMain()