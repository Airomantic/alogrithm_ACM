"""
10 9 2 5 3 7 101 18 19 20 14 21
dp=[1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 4, 7]
跟俄罗斯套娃一样    
"""
class Solution:

    def lengthOfLIS(self, num):
        if not num:
            return 0
        dp=[]
        for i in range(len(num)):
            dp.append(1) #相当于初始化记录递增子串长度，在i=4的循环dp=[1,1,1,1],之后dp[4]会被覆盖
            for j in range(i): #j=2,i=3
                if num[i]>num[j]: #只要前面有比当前小的，dp[i]就从当前递增那个数不变，除非有新的更大的数时，dp[j]+1再记录加1
                    dp[i]=max(dp[i],dp[j]+1) #dp[j]加1是为了每次遇到递增数字，状态转移dp数组当前元素是上一个元素+1
        print(dp)
        return max(dp)

while True:
    try:
        num=list(map(int,input().strip().split(" ")))
        print(num)
        res=Solution().lengthOfLIS(num)
        print(res)
    except:
        break