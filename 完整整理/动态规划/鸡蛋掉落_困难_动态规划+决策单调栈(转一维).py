
"""
https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution-2/
视频：https://leetcode-cn.com/problems/super-egg-drop/solution/ke-shi-hua-dpguo-cheng-by-alchemist-5r/
状态描述：

动态规划表练习：
https://alchemist-al.com/algorithms/egg-dropping-problem
"""


class Solution:

    def superEggDrop(self, eggs, floors):
        #dp[i] 代表 dp[1,i]
        dp=list(range(floors+1))
        dp2=[0]*(floors+1)
        for eggs in range(2,eggs+1):
            #dp2[i] = dp(j, i)
            x=1
            for floors in range(1,floors+1):
                # 发现dp2[floors] = dp(j, floors)
                #增加最优x
                #注意max(dp[x-1], dp2[m-x]) >= max(dp[x], dp2[m-x-1])简化了max(T1(x-1), T2(x-1)) >= max(T1(x), T2(x))
                while x<floors and max(dp[x-1],dp2[floors-x])>= max(dp[x],dp2[floors-x-1]):
                    x+=1
                #最终答案在x处
                dp2[floors]=1+max(dp[x-1],dp2[floors-x])
            dp=dp2[:]
        return dp[-1]

if __name__ == '__main__':
    all=list(map(int,input().strip().split()))
    # while True:
    start=all[0]
    target=all[1]
    res=Solution().superEggDrop(start,target)
    print(res)
