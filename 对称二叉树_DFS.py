import io
import sys

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def stringToTreeNode(input):
    input=input.strip() #去掉[]
    input=input[1:-1]
    if not input:
        return None
    inputValues=[s.strip() for s in input.split(',')] #记得加中括号
    root=TreeNode(int(inputValues[0]))
    nodeQueue=[root] #声明一个list表示队列，并且内部存储结构是二叉树
    front=0
    index=1
    while index<len(inputValues):
        node=nodeQueue[front] #声明构造一个nodeQueue队头，用于之后引导node.left和node.right等左右孩子结点
        front=front+1 #前继结点

        item_left=inputValues[index]
        index=index+1
        if item_left!="null":
            leftNumber=int(item_left) #注意：需先强转成integer
            node.left=TreeNode(leftNumber) #注意调用的是TreeNode类用()，不是中括号
            nodeQueue.append(node.left)

        if index>=len(inputValues):
            break

        item_right = inputValues[index]
        index = index + 1
        if item_right!="null":
            rightNumber = int(item_right)  # 注意：需先强转成integer
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

    return root

class Solution:
    def isSymmetrical(self, root:TreeNode):
        if not root:
            return None

        def DFS(left,right):
            if not (left or right): #注意，表示左右子树任何一个都没有，即只有一个根结点属于对称树
                return True
            if not (left and right): #左子树和右子树只有一颗没有（为空），返回不对称
                return False
            if left.value!=right.value: #如果左右对称点的val不来源同一个根结点，返回True序要满足下一行代码的递归
                return True
            return DFS(left.left, right.right) and DFS(left.right,right.left) #否则返回
        return DFS(root.left,root.right) #先调用DES，传入TreeNode的左右子树
"""
    def isSymmetrical2(self, root: TreeNode):
        def isMirror(left:TreeNode,right:TreeNode):
            if left=="null" and right=="null":
                return True
            if left=="null" or right=="null":
                return False
            return left.val==right.val and isMirror(left.left, right.right) and isMirror(left.right,right.left)
        return isMirror(root,root)
"""
def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    while True:
        try:
            line=next(lines)
            node=stringToTreeNode(line)
            result=Solution().isSymmetrical(node)
            out=str(result)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    EnterMain()