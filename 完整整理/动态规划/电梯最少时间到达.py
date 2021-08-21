

"""
问题：
电梯一次上升或下降一层，用时记为1s，可以从第n层快速到第2n层或从第2n层到第n层同样用时1s，
求从第5层到17层的最少用时，如5->10->9->18->17，用时4s，请用程序设计任一层到另一层的最小用时？
分两步走：
1.一步一步靠近 d[i][0]=target-start 所有的状态都转化成向上的

"""
import io
import sys



class Solution:

    def Elevator_leastTime(self, start,target):
        '''
        dp[i][0]表示只有一颗蛋去检测i层楼需要的最小次数；  也可以写成 dp[0][i]
        dp[i][1]表示有两颗蛋去检测i层楼需要的最小次数。             dp[1][i]
        '''
        dp=[[float('inf')]*2 for start in range(target+1)]
        dp[0]=[0,0]
        if start>target:
            self.Elevator_leastTime(target,start)
        for i in range(start,target+1): #不管是上还是下
            dp[i][0]=target-i
            for k in range(start,i+1):
                """状态转移"""

                dp[i][1]=min(dp[i][1],max(dp[k-1][0],dp[i-k][1])  +1 ) #注意+1要写出来
        return dp[target][1]


if __name__ == '__main__':
    all=list(map(int,input().strip().split()))
    while True:
        start=all[0]
        target=all[1]
        res=Solution().Elevator_leastTime(start,target)
        print(res)