# Definition for a binary tree node.
"""
-10 9 20 null null 15 7
输出：42    解释：15->20->7 之和
"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        #初始化设置无穷小
        self.maxSum = float("-inf") #__init__ 是为了设置全局变量

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0 #None表示结点，0表示null
            """总是先往叶子结点查找"""
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0) #防止负数,比如-10，但如果负数连接结点必须加上
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.value + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath) #self.maxSum初始值是float("-inf")无穷小的一个数值

            # 返回节点的最大贡献值
            return node.value + max(leftGain, rightGain) #这里的node.value会被递归函数获取

        maxGain(root)
        return self.maxSum


def stringToTreeNode(input):
    # input = input.strip()
    # input = input[1:-1]
    # if not input:
    #     return None
    #
    # inputValues = [s.strip() for s in input.split(',')]
    inputValues=input.strip().split(" ") #自动生成list
    print(inputValues,type(inputValues))
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root] #声明构造
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]   #从0开始 仅仅队列上的"位置"
        front = front + 1

        item = inputValues[index] #从1开始 赋给左右孩子结点"值"
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues): #注意是 >=
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root #root = TreeNode(int(inputValues[0])) 初始化声明的好处


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().maxPathSum(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()