import json
from typing import List

"""
输入：
4
[1,-1,3,-1]
[2,-1,-1,-1]
输出：true
输入：
4
[1,-1,3,-1]
[2,3,-1,-1]
输出：false
"""
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        n1 = n
        if n == 1 and leftChild[0] == -1 and rightChild[0] == -1:
            return True

        for indx, i in enumerate(leftChild):
            if i != -1:  # 有孩子节点
                # 该节点已有父节点 或跟自己的子节点强连通
                if parent[i] != -1 or leftChild[i] == indx or rightChild[i] == indx:
                    return False
                else:
                    parent[i] = indx
                    n1 -= 1

        for indx, i in enumerate(rightChild):
            if i != -1:
                if parent[i] != -1 or leftChild[i] == indx or rightChild[i] == indx:
                    return False
                else:
                    parent[i] = indx
                    n1 -= 1

        # 有多个根节点
        if n1 != 1:
            return False
        else:
            for indx, i in enumerate(parent):  # 找唯一根节点
                if i == -1:
                    if (leftChild[indx] != -1 or rightChild[indx] != -1):  # 唯一根节点有子节点
                        return True
                    else:
                        return False
            return True


def stringToIntegerList(input):
    return json.loads(input)


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
            n = int(line);
            line = next(lines)
            leftChild = stringToIntegerList(line);
            line = next(lines)
            rightChild = stringToIntegerList(line);

            ret = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()