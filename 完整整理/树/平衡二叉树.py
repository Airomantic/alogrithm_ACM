import io
import sys
"""
3 9 20 null null 15 7

"""

class Solution:

    def isBalanced(self, root):
        def height(root): #寻求左右子树最大值
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1

        """通过递归缩进到满足都有root条件，返回True"""
        if not root:
            return True

        return abs(height(root.left)-height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)#递归
class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


def stringToTreeNode(input):
    if not input:
        return None
    inputValues=[s.strip() for s in input.split(" ")] #封装成list
    # print(inputValues)
    root=TreeNode(int(inputValues[0]))
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

def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')
    lines=readlines()
    # while True:
    #     try:
    line=next(lines)
    root=stringToTreeNode(line)
    res=Solution().isBalanced(root)
    print(res)
        # except:
        #     break

if __name__ == '__main__':
    main()