import io
import sys
"""
1 null 3 2 4 null 5 6
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
def stringToTreeNode(input):
    if not input:
        return None
    inputValues=[s.strip() for s in input.split()]
    print(inputValues)
    root=Node(int(inputValues[0]))
    nodeQueue=[root]
    front=0
    index=1
    while index<len(inputValues):
        node =nodeQueue[front]
        front+=1

        item=inputValues[index]
        index+=1
        if item!="null":
            childrenNumber=int(item)
            node.children=Node(childrenNumber)
            nodeQueue.append(node.children)

        if index>=len(inputValues):
            break
    """返回root，记得写到while外面"""
    return root
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0

        def dfs(root):
            dep = [0, 0]
            if root:
                for ch in root.children:
                    dep.append(dfs(ch))
                dep.sort(reverse=True)
            self.res = max(self.res, sum(dep[:2]))
            return dep[0] + 1

        dfs(root)
        return self.res


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
            root = stringToTreeNode(line)

            ret = Solution().diameter(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()