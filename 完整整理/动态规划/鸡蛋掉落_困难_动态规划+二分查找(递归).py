
"""
https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution-2/
视频：https://leetcode-cn.com/problems/super-egg-drop/solution/ke-shi-hua-dpguo-cheng-by-alchemist-5r/
状态描述：

动态规划表练习：
https://alchemist-al.com/algorithms/egg-dropping-problem
"""


class Solution:

    def superEggDrop(self, eggs, floors):
        memo={} #记录
        def dp(eggs,floors):
            if (eggs,floors) not in memo:
                if floors==0:
                    ans=0
                elif eggs==1:
                    ans=floors
                else:
                    low,high=1,floors
                    #保持2个x值的差距，以便以后手动检查
                    while low+1<high:
                        x=(low+high)//2
                        t1=dp(eggs-1,x-1)
                        t2=dp(eggs,floors-x) #碎了

                        if t1<t2: #碎了往上走二分
                            low=x
                        elif t1>t2: #没碎往下二分
                            high=x
                        else:
                            low=high=x
                    ans=1+min( max(dp(eggs-1,x-1) ,dp(eggs,floors-x) )
                               for x in (low,high))
                memo[eggs,floors]=ans #每次循环记录新的，用于查看当前eggs,floors是否在里面
            return memo[eggs,floors]

        return dp(eggs,floors)

if __name__ == '__main__':
    all=list(map(int,input().strip().split()))
    # while True:
    start=all[0]
    target=all[1]
    res=Solution().superEggDrop(start,target)
    print(res)
