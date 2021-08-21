import io
import sys

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def stringToTreeNode(input):
    input=input.strip() #去掉空格
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