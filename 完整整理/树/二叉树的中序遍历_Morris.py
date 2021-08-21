import io
import sys
"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
"""
class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def stringToTreeNode(input):
    if not input:
        return None
    input=input.strip()
    input=input[1:-1]
    inputValues=[s.strip() for s in input.split(",")] #注意s
    root= TreeNode(int(inputValues[0]))
    nodeQueue=[root]
    front=0
    index=1
    while index<len(inputValues): #注意针对的是inputValues，没有=
        node=nodeQueue[front]
        front+=1  #注意front

        item=inputValues[index]
        index+=1
        if item!="null":
            leftNumber=int(item)
            node.left=TreeNode(leftNumber)
            nodeQueue.append(node.left)
        """判个空"""
        if index>=len(inputValues):
            break

        item = inputValues[index]
        index += 1
        if item!="null":
            rightNumer=int(item)
            node.right=TreeNode(rightNumer)
            nodeQueue.append(node.right)
    return root

class Solution:
    def inorderTraversal(self,root):
        """中序"""
        res=[]
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
        # try:
        line=next(lines)
        root=stringToTreeNode(line)
        res=Solution().inorderTraversal(root)
        print(res)
        # except: #有这个出错就不会报错，不知道错在哪
        #     break
if __name__ == '__main__':
    main()