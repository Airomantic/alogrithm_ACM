
"""
https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution-2/
视频：https://leetcode-cn.com/problems/super-egg-drop/solution/ke-shi-hua-dpguo-cheng-by-alchemist-5r/
状态描述：（k,N），则当从第x楼仍鸡蛋的时候
鸡蛋不碎，状态变成(k,N-x)        f[i-1][j]
鸡蛋碎，状态变成 (k-1,x-1)       f[i-1][j-1]
动态规划表练习：
https://alchemist-al.com/algorithms/egg-dropping-problem
"""


class Solution:

    def superEggDrop(self, eggs, floors):
        if floors==1:
            return 1
        f=[[0]*(eggs+1) for _ in range(floors+1)]
        for i in range(1,eggs+1):
            f[1][i]=1 #第一层楼第i个鸡蛋
        ans=-1
        for i in range(2,floors+1):
            for j in range(1,eggs+1):
                f[i][j]=1+f[i-1][j-1]+f[i-1][j]  #还需要测试的最坏次数
            if f[i][eggs]>=floors:
                ans=i #i>=2
                break
        return ans

if __name__ == '__main__':
    all=list(map(int,input().strip().split()))
    while True:

        start=all[0]
        target=all[1]
        res=Solution().superEggDrop(start,target)
        print(res)
