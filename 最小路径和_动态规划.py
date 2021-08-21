
import json
from typing import List
"""
[[1,3,1],[1,5,1],[4,2,1]]
7
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:  # 行或列为空
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]  # 定义同等行列数dp[][]并初始化为[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        print(dp)
        """dp初始化第一个元素左上角"""
        dp[0][0] = grid[0][0]
        """dp初始化第一行和第一列所有的元素"""
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]  # 选行方向

        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]  # 选列方向

        """dp计算所有元素前后左右最小相邻元素和"""
        for i in range(1, rows):
            for j in range(1, columns):

                # 比较逆方向上的 左和上一位的大小，选择小的相加，构成新的dp[i][j]
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]  # 从右下往左上推进，以保证从左上向右下选取最佳路径（两个值最小的）

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
            twoD = stringToIntegerList(line)
            ret = Solution().minPathSum(twoD)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()