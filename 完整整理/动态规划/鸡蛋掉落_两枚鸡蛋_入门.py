

"""
https://leetcode-cn.com/problems/egg-drop-with-2-eggs-and-n-floors/solution/fu-za-du-cong-on2dao-o1de-liu-chong-jie-k3uti/
https://leetcode-cn.com/problems/egg-drop-with-2-eggs-and-n-floors/solution/python-xiang-xi-tong-su-di-jie-du-dong-t-nb8t/
i-k: 楼层向下沉下去k层，从k作为第一次开始，可能碎的界限f=i，需要检测i-k，
这是没碎的情况，所以状态转移-递归就能将2个鸡蛋🥚进行一个任一试探，另一个一步一步来检测的循环传递状态
k-1：是碎了的情况
"""
import io
import sys


def readlines():
    for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
        yield lines.strip('\n')


class Solution:

    def twoEggDrop(self, n):
        '''
        dp[i][0]表示只有一颗蛋去检测i层楼需要的最小次数；  也可以写成 dp[0][i]
        dp[i][1]表示有两颗蛋去检测i层楼需要的最小次数。             dp[1][i]
        '''
        dp=[[float('inf')]*2 for _ in range(n+1)]
        dp[0]=[0,0]
        for i in range(1,n+1):
            dp[i][0]=i
            for k in range(1,i+1):
                """状态转移"""
                dp[i][1]=min(dp[i][1],max(dp[k-1][0],dp[i-k][1])  +1 ) #注意+1要写出来
        return dp[n][1]


if __name__ == '__main__':
    lines=readlines()
    while True:
        line=next(lines)
        n=int(line)
        res=Solution().twoEggDrop(n)
        print(res)