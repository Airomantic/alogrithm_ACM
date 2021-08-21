"""
动态规划
状态转移方程: dp
f(0)=0,f(1)=1,f(2)=1,f(3),=2,f(4)=2,f(5)=2    =>  f(i)=,i:coin面值   => amount
https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
输入：
[1, 2, 5] 11
1 2 5 11
dp:[0,1,1,2,2,1,2,2,3,3,2,3]
关键点： need_numbers=dp[need_money] 建立起还需金额和还需硬币总数量
"""

class Solution:

    def coinChange(self, coins, amount):
        ##初始化状态转移方程的元素值都为无穷大，因为第一位设置为0，所以之后元素个数是amount，总的需要+1
        dp=[float('inf')]*(amount+1)
        dp[0]=0 #设置状态转移方程第一位从0开始
        for coin in coins:
            for x in range(coin,amount+1): #注意amount+1需要加1，因为x的终止数是(amount+1)-1
                dp[x]=min(dp[x],dp[x-coin]+1) #x-coin每次还需硬币总金额，dp[x-coin]还需要硬币数量
        return dp[amount] if dp[amount]!=float('inf') else -1 #最后弹出dp[11]

while True:
    try:
        all=list(map(int,input().strip().split(" ")))
        coins,amount=all[:-1],all[-1]
        print(coins,amount)
        res=Solution().coinChange(coins,amount)
        print(res)
    except:
        break
