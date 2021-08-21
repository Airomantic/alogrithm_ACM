import io
import json
import sys
"""
输入：
[1,4,2,3]
1
输出：
2
解释：4变成2：4-2=2
输入：
[3,5,4,7]
2
输出：
1
解释：7变成6：7-6=1
"""

def stringToIntegerList(input):
    return json.loads(input)


class Solution:
    def MinAdjustmentCost(self, A, target):
        if not A:
            return 0
        m, n = len(A), max(A)
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                f[i][j] = abs(A[i] - j - 1)
        for i in range(1, m):
            for j in range(n):
                f[i][j] += min(f[i - 1][max(0, j - target):min(n, j + target + 1)])
        return min(f[-1])

def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    while True:
        try:
            line=next(lines)
            list=stringToIntegerList(line)
            line2=next(lines)
            target=int(line2)
            result=Solution().MinAdjustmentCost(list,target)
            print(result)
        except StopIteration:
            break

if __name__ == '__main__':
    main()