
import json
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid and grid[0]: #注意是and
            return None
        row,col=len(grid),len(grid[0])
        dp=[[0]*col for _ in range(row)]
        dp[0][0]=grid[0][0]
        for i in range(1,row):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,col):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        #继续计算所有上下左右相邻元素最小和
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[row-1][col-1]

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